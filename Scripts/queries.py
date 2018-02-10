import sys
sys.path.append("./../Analysis")
import os
os.environ['ETH_BLOCKCHAIN_ANALYSIS_DIR'] = './../Analysis/'
import pymongo
import json
import datetime




if __name__=="__main__":

    block_max = 4369999
    quadrillion = 1000000000000000000

    cmd = "(mongod --dbpath {} > {}/mongo.log 2>&1) &".format(
        "/mnt/c/data/db",
        "/mnt/c/data/anaLogs")

    client = pymongo.MongoClient(serverSelectionTimeoutMS=1000)
    collection=client["blockchainExtended2"]["blocks"]


    with open('genesis_block.json') as data_file:
        data = json.load(data_file)

    genesisAddresses = []
    commulatedGenesisEther=0
    for addr in data:
        #genesisAddresses.append(data[addr])
        #print(data[addr])
        #print(data[addr]["wei"])
        genesisAddresses.append("0x" + addr)
        commulatedGenesisEther+=float(data[addr]["wei"])
        print(commulatedGenesisEther)




    fourWeeks = 2419200
    interval = fourWeeks

    startTime = 1435622400

    genesisEtherToCertainTime = {}

    while startTime < 1508112000:
        print(datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S'))
        txsInInterval = collection.aggregate([{ "$match" : {"$and":[{ "timestamp" : {"$lt":(startTime+interval) }},{"timestamp" : {"$gte":startTime }}] }},{ "$unwind" : '$transactions'}])
        startTime+=interval
        for i in txsInInterval:
            if i["transactions"]["from"] in genesisAddresses:
                if float(data[i["transactions"]["from"][2:]]["wei"]) >=0:
                    ether=i["transactions"]["value"]
                    if float(data[i["transactions"]["from"][2:]]["wei"])<=ether*quadrillion:
                        data[i["transactions"]["from"][2:]]["wei"]=0
                        commulatedGenesisEther-=data[i["transactions"]["from"][2:]]["wei"]
                    else:
                        data[i["transactions"]["from"][2:]]["wei"]= float(data[i["transactions"]["from"][2:]]["wei"])-ether*quadrillion
                        commulatedGenesisEther-=ether*quadrillion

            print(commulatedGenesisEther)

        genesisEtherToCertainTime[startTime]=commulatedGenesisEther

        with open('losingEther.txt', 'w') as outfile:
            json.dump(genesisEtherToCertainTime, outfile)




    print("DONE")


    # txs = collection.aggregate([{ "$unwind" : '$transactions'}])
    #
    # for i in txs:
    #     if i["transactions"]["from"] in genesisAddresses:
    #         print(i["transactions"]["from"])
    #         print(i["number"])
       # print(datetime.datetime.fromtimestamp(i["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'))