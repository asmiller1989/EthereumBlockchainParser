import json

with open('data/getTopTokens.json') as tokenData:
	tokenData = json.load(tokenData)

for i in tokenData['tokens']:
	print(i['address'])

with open('dollarPrice.json') as data_file:
	data = json.load(data_file)

for i in data:
	print(i["close"])
