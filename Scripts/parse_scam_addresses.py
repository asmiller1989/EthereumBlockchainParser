import json
import collections




with open('data/scam_addresses.json') as data_file:
    data = json.load(data_file)

addresses={}



for scam in data:
	addresses[scam]=6

with open('scam_addresses.json', 'w') as outfile:
    json.dump(addresses, outfile)