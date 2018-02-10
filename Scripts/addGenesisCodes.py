import pickle
import json

state = pickle.load(open(".contracts.p", "rb"))

with open('genesis_block.json') as data_file:
	data = json.load(data_file)


genesisAddresses=[]
addresses = state[1]
for addr in data:
	genesisAddresses.append("0x"+addr)

counter=1
for d in genesisAddresses:
	if d in addresses:
		print(counter)
		counter+=1
	addresses[d] = 6

sum = sum(x == 6 for x in addresses.values())
print(sum)

pickle.dump(addresses, open(".addresses.p", "wb"))

#for address in addresses:
#	print(counter)
#	counter+=1