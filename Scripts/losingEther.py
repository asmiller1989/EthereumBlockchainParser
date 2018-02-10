import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import json
import collections


with open('losingEther.json') as data_file:
    data = json.load(data_file)

x=[]
y=[]
quadrillion = 1000000000000000000

ordered= collections.OrderedDict(sorted(data.items()))


for i in ordered:
	y.append(data[i]/quadrillion)

for i in ordered.keys():
	x.append(int(i))

#values=[y*dp for y,dp in zip(y,dollarPrice)]


plt.figure()
plt.plot(np.array(x),np.array(y))
plt.axis([min(x), max(x),0,max(y)])
plt.savefig("genesisEther.svg")
