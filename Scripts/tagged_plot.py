import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import json
import collections
import seaborn as sns


def plotttt(filename):
	return true



with open('from_tags_final.json') as data_file:
    data = json.load(data_file)



x=[]
y=[]
volumes={}

quadrillion = 1000000000000000000

ordered= collections.OrderedDict(sorted(data.items()))

tags=['1','2','3','4','5','6','7','8','9']#'10']

legend=['exchanges','TOKENS','miningPools','singularDTV','ETHDEV','Scam','WeirdSplits','ETHDEV','ForkContract']#,'Other']


for timepoint in ordered:
	volume=0
	for tag in tags:
		volume+=data[timepoint][tag][2]
	volumes[timepoint]=volume
	#tagValues.append(data[timepoint][tag])


for tag in tags:
	tagValues=[]
	for timepoint in ordered:
		tagValues.append(data[timepoint][tag][2]/max(1,volumes[timepoint]))
	y.append(tagValues)


for i in ordered.keys():
	x.append(int(i))

#values=[y*dp for y,dp in zip(y,dollarPrice)]



fig = plt.figure()
ether = fig.add_subplot(2,2,1)
#dollar = fig.add_subplot(2,2,2)
#number = fig.add_subplot(2,2,3)
pal = sns.color_palette("Set1")
ether.stackplot(x,y,labels=tags,colors=pal, alpha=0.4 )
plt.legend(loc='upper right')
ether.legend(legend,bbox_to_anchor=(1.05, 1),loc=2, borderaxespad=0.,fontsize=5)



fig.savefig("tagged_to_plot_stacked.svg")


#   https://python-graph-gallery.com/255-percentage-stacked-area-chart/
