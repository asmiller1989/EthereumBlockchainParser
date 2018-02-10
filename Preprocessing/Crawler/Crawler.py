"""A client to interact with node and to save data to mongo."""

from pymongo import MongoClient
import crawler_util
import requests
import json
import sys
import os
import logging
import time
import tqdm
sys.path.append(os.path.realpath(os.path.dirname(__file__)))

DIR = "/mnt/c/data/db"
LOGFIL = "crawler.log"
if "BLOCKCHAIN_ANALYSIS_LOGS" in os.environ:
    LOGFIL = "{}/{}".format(os.environ['BLOCKCHAIN_ANALYSIS_LOGS'], LOGFIL)
crawler_util.refresh_logger(LOGFIL)
logging.basicConfig(filename=LOGFIL, level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class Crawler(object):
    """
    A client to migrate blockchain from geth to mongo.

    Description:
    ------------
    Before starting, make sure geth is running in RPC (port 8545 by default).
    Initializing a Crawler object will automatically scan the blockchain from
    the last block saved in mongo to the most recent block in geth.

    Parameters:
    -----------
    rpc_port: <int> default 8545 	# The port on which geth RPC can be called
    host: <string> default "http://localhost" # The geth host
    start: <bool> default True		# Create the graph upon instantiation

    Usage:
    ------
    Default behavior:
        crawler = Crawler()

    Interactive mode:
        crawler = Crawler(start=False)

    Get the data from a particular block:
        block = crawler.getBlock(block_number)

    Save the block to mongo. This will fail if the block already exists:
        crawler.saveBlock(block)

    """


    def __init__(
        self,
        start=True,
        rpc_port=8545,
        host="http://localhost",
        delay=0.0001
    ):
        """Initialize the Crawler."""
        print("Starting Crawler")
        self.url = "{}:{}".format(host, rpc_port)
        self.headers = {"content-type": "application/json"}

        # Initializes to default host/port = localhost/27017
        self.mongo_client = crawler_util.initMongo(MongoClient())
        # The max block number that is in mongo
        self.max_block_mongo = None
        # The max block number in the public blockchain
        self.max_block_geth = None
        # Record errors for inserting block data into mongo
        self.insertion_errors = list()
        # Make a stack of block numbers that are in mongo
        self.block_queue = crawler_util.makeBlockQueue(self.mongo_client)
        # The delay between requests to geth
        self.delay = delay

        self.session=requests.Session()

        if start:
            self.max_block_mongo = self.highestBlockMongo()
            self.max_block_geth =  4369999 #self.highestBlockEth()
            self.run()

    def _rpcRequest(self, method, params, key):
        """Make an RPC request to geth on port 8545."""
        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": 0
        }
        """time.sleep(self.delay)"""
        data=json.dumps(payload)
        res = self.session.post(
              self.url,
              data, stream=True).json()
        return res[key]

    def getBlock(self, n):
        """Get a specific block from the blockchain and filter the data."""

        data = self._rpcRequest("eth_getBlockByNumber", [n, True], "result")
        block = crawler_util.decodeBlock(data)
        uncleHash = data["hash"]
        if data["uncles"]:
            uncles = self.retrieveUncles(uncleHash,block["number"])
            block["uncles"] = uncles
        return block

    def getMiner(self, n):
        miner = self._rpcRequest("eth_getBlockByNumber", [hex(n), False], "result")["miner"]
        crawler_util.insertMiner(self.mongo_client,n,miner)



    def retrieveUncles(self, blockHash, height):
        # {
        #     "jsonrpc": "2.0",
        #     "id": 1,
        #     "result": {
        #         "difficulty": "0x57f117f5c",
        #         "extraData": "0x476574682f76312e302e302f77696e646f77732f676f312e342e32",
        #         "gasLimit": "0x1388",
        #         "gasUsed": "0x0",
        #         "hash": "0x932bdf904546a2287a2c9b2ede37925f698a7657484b172d4e5184f80bdd464d",
        #         "logsBloom": "0x000000",
        #         "miner": "0x5bf5e9cf9b456d6591073513de7fd69a9bef04bc",
        #         "mixHash": "0x4500aa4ee2b3044a155252e35273770edeb2ab6f8cb19ca8e732771484462169",
        #         "nonce": "0x24732773618192ac",
        #         "number": "0x299",
        #         "parentHash": "0xa779859b1ee558258b7008bbabff272280136c5dd3eb3ea3bfa8f6ae03bf91e5",
        #         "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        #         "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
        #         "size": "0x21d",
        #         "stateRoot": "0x2604fbf5183f5360da249b51f1b9f1e0f315d2ff3ffa1a4143ff221ad9ca1fec",
        #         "timestamp": "0x55ba4827",
        #         "totalDifficulty": null,
        #         "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
        #         "uncles": []
        #     }
        # }

        uncleCountHex = self._rpcRequest("eth_getUncleCountByBlockHash",[blockHash],"result")
        uncleCount = int(uncleCountHex, 16)
        uncles = []
        for i in range(uncleCount):
            uncleBlock = self._rpcRequest("eth_getUncleByBlockHashAndIndex",[blockHash,hex(i)],"result")
            newBlock = {
               "miner":uncleBlock["miner"],
               "reward": (8 - (height-int(uncleBlock["number"], 16))) / 8 * 5
              # "reward": (8 - (int(uncleBlock["number"], 16)-height)) / 8 * 5 ==> 10-reward
            }
            uncles.append(newBlock)
        return uncles

    def highestBlockEth(self):
        """Find the highest numbered block in geth."""
        num_hex = self._rpcRequest("eth_blockNumber", [], "result")
        return int(num_hex, 16)

    def saveBlock(self, block):
        """Insert a given parsed block into mongo."""
        e = crawler_util.insertMongo(self.mongo_client, block)
        if e:
            self.insertion_errors.append(e)

    def saveMiner(self, block):
        """Insert a given parsed block into mongo."""
        e = crawler_util.insertMiner(self.mongo_client, block)
        if e:
            self.insertion_errors.append(e)

    def highestBlockMongo(self):
        """Find the highest numbered block in the mongo database."""
        highest_block = crawler_util.highestBlock(self.mongo_client)
        logging.info("Highest block found in mongodb:{}".format(highest_block))
        return highest_block

    def add_block(self, n):
        """Add a block to mongo."""

        b = self.getBlock(n)
        if b:
            self.saveBlock(b)
            time.sleep(0.001)
        else:
            self.saveBlock({"number": n, "transactions": []})


    def add_miner(self, n):
        """Add a block to mongo."""

        self.getMiner(n)
       # else:
        #    self.saveBlock({"number": n, "transactions": []})

    def run(self):
        """
        Run the process.

        Iterate through the blockchain on geth and fill up mongodb
        with block data.
        """
        print("Processing geth blockchain:")
        print("Highest block found as: {}".format(self.max_block_geth))
        print("Number of blocks to process: {}".format(
            len(self.block_queue)))

        # Make sure the database isn't missing any blocks up to this point
        logging.debug("Verifying that mongo isn't missing any blocks...")
        self.max_block_mongo = 1
        if len(self.block_queue) > 0:
            print("Looking for missing blocks...")
            self.max_block_mongo = self.block_queue.pop()
            for n in tqdm.tqdm(range(1, self.max_block_mongo)):
                if len(self.block_queue) == 0:
                    # If we have reached the max index of the queue,
                    # break the loop
                    break
                else:
                    # -If a block with number = current index is not in
                    # the queue, add it to mongo.
                    # -If the lowest block number in the queue (_n) is
                    # not the current running index (n), then _n > n
                    # and we must add block n to mongo. After doing so,
                    # we will add _n back to the queue.
                    _n = self.block_queue.popleft()
                    if n != _n:
                        self.add_block(n)
                        self.block_queue.appendleft(_n)
                        logging.info("Added block {}".format(n))

        # Get all new blocks
        print("Processing remainder of the blockchain...")
        for n in tqdm.tqdm(range(self.max_block_mongo, self.max_block_geth)):
            self.add_block(hex(n))
        #for n in tqdm.tqdm(range(3826871, self.max_block_geth)):
         #  self.add_miner(n)

        print("Done!\n")
