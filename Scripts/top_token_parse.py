import json
import collections




with open('data/getTopTokens.json') as data_file:
    data = json.load(data_file)

addresses={}



for token in data:
	addresses[token['address']]=2

with open('token_addresses.json', 'w') as outfile:
    json.dump(addresses, outfile)