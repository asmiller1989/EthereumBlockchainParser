"""Various 'special' addresses that should be tagged."""

from collections import defaultdict

# Exchange wallets = 1
# Crowdsale wallets = 2
# Mining pools = 3
tags = defaultdict(int, {
    "0x32be343b94f860124dc4fee278fdcbd38c102d88": 1,  # Polo hot wallet
    "0xb794f5ea0ba39494ce839613fffba74279579268": 1,  # Polo cold wallet
    "0x2910543af39aba0cd09dbb2d50200b3e800a63d2": 1,  # Kraken
    "0x120a270bbc009644e35f0bb6ab13f95b8199c4ad": 1,  # Shapeshift
    "0xcafb10ee663f465f9d10588ac44ed20ed608c11e": 1,  # Bitfinix
    "0x40b9b889a21ff1534d018d71dc406122ebcf3f5a": 1,  # Gatecoin
    "0x42da8a05cb7ed9a43572b5ba1b8f82a0a6e263dc": 1,  # Yunbi 1
    "0xd94c9ff168dc6aebf9b6cc86deff54f3fb0afc33": 1,  # Yunbi 2
    "0xbb9bc244d798123fde783fcc1c72d3bb8c189413": 2,  # DAO
    "0x807640a13483f8ac783c557fcdf27be11ea4ac7a": 2,  # DAOextrabalance
    "0xf0160428a8552ac9bb7e050d90eeade4ddd52843": 2,  # Digix
    "0x2a65aca4d5fc5b5c859090a6c34d164135398226": 3,  # Dwarfpool
    "0x151255dd9e38e44db38ea06ec66d0d113d6cbe37": 3,  # Dwarfpool2
    "0x63a9975ba31b0b9626b34300f7f627147df1f526": 3,  # eth.supernova.cc
    "0xf8b483dba2c3b7176a3da549ad41a48bb3121069": 3,  # coinotron
    "0xea674fdde714fd979de3edf0f56aa9716b898ec8": 3,  # ethermine
    "0x4bb96091ee9d802ed039c4d1a5f6216f90f81b01": 3,  # ethpool
    "0x1dcb8d1f0fcc8cbc8c2d76528e877f915e299fbe": 3,  # supernova
    "0xa027231f42c80ca4125b5cb962a21cd4f812e88f": 3,  # eth.ppa.ua
    "0x0c729be7c39543c3d549282a40395299d987cec2": 3,  # ?
    "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5": 3,  # Nanopool
    "0x68795c4aa09d6f4ed3e5deddf8c2ad3049a601da": 3,  # coinmine.pl
    "0x61c808d82a3ac53231750dadc13c777b59310bd9": 3,  # f2pool
    "0xe6a7a1d47ff21b6321162aea7c6cb457d5476bca": 3,  # ethpool
    "0x9d551f41fed6fc27b719777c224dfecce170004d": 3,  # ethereumpool
    "0xd1e56c2e765180aa0371928fd4d1e41fbcda34d4": 3,  # weipool
    "0xf3b9d2c81f2b24b0fa0acaaa865b7d9ced5fc2fb": 3,  # bitclubpool
    "0xb2930b35844a230f00e51431acae96fe543a0347": 3,  # mininggpoolhub
    "0xe853c56864a2ebe4576a807d26fdc4a0ada51919": 1,  # Kraken_3
    "0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98": 1,  #Bittrex
    "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae": 5,  #ETHDEV
    "0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be": 1, #Binance
    "0xc78310231aa53bd3d0fea2f8c705c67730929d8f": 4, #singularDTV
    "0x267be1c1d684f78cb4f6a176c4911b741e4ffdc0": 1, #Kraken_4
    "0x0a869d79a7052c7f1b55a8ebabbea3420f0d1e13": 1, #Kraken_2
    "0x4fdd5eb2fb260149a3903859043e962ab89d8ed4": 1, #Bitfinex_3
    "0xB3764761E297D6f121e79C32A65829Cd1dDb4D32": 6, #SCAAAAM HACKER
    "0x6a164122d5cf7c840d26e829b46dcc4ed6c0ae48": 6,  #FAKE_Coindash SCAM
    "0xD4914762f9BD566Bd0882B71af5439c0476D2Ff6": 6,  #HACK
    "0x1342A001544B8b7ae4a5d374e33114C66d78bd5f": 6,  #HACK2
    "0x2910543Af39abA0Cd09dBb2D50200b3E800A63D2": 1,  #KRAKEN_1
    "0x8271b2e8cbe29396e9563229030c89679b9470db": 1,  #liqui.io
    "0x876eabf441b2ee5b5b0554fd502a8e0600950cfa": 1,  #Bitfinex_4
    "0xab7c74abc0c4d48d1bdad5dcb26153fc8780f83e": 2,   #Bitfinex 2?
    "0xB2D7e6CD1b25F591e2E630Ba65DAC638e6cd4C8e": 8, # ETHDEV. Mined first Blocks 90000?
    "0x536c2622748118a82bc9fb15a450d828966d9761": 9, # FORK CONTRACT:O
    "0x53d284357ec70cE289D6D64134DfAc8E511c8a3D": 1,  #Exchange (Polo or Kraken)
    "0xf4B51B14b9EE30dc37EC970B50a486F37686E2a8": 1 , #bitfinex Cold + ERC TOKENS
    "0x281055afc982d96fab65b3a49cac8b878184cb16": 7,# MAYBE SCAM, weird INS
    "0x6f46cf5569aefa1acc1009290c8e043747172d89": 7, # same weirst SHIT
    "0x90e63c3d53e0ea496845b7a03ec7548b70014a91": 7, #same weird Stuff
    "0x61EDCDf5bb737ADffE5043706e7C5bb1f1a56eEA": 1, #Gemini Cold Wallet
    "0xf1ce0a98efbfa3f8ebec2399847b7d88294a634e": 1, #Bitfinex Cold Wallet

})
