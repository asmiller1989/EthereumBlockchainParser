import matplotlib
matplotlib.use('Agg')
from pylab import *
import time
from graph_tool.all import *
import graph_tool
import numpy
import matplotlib.pyplot as plt
from collections import Counter

t = time.time()
print("Starting at: " + str(time.time()-t))

tmp_graph = load_graph("data/graphs/4369999_None.gt")


print("loaded After: " + str(time.time()-t))


indegrees = []
outdegrees = []
comdegrees = []


for i in tmp_graph.vertices():
	indegrees.append(i.in_degree())
print("In After: " + str(time.time()-t))

for i in tmp_graph.vertices():
	outdegrees.append(i.out_degree())
print("Out After: " + str(time.time()-t))

for i in tmp_graph.vertices():
	comdegrees.append(i.out_degree()+i.in_degree())
print("Commulated After: " + str(time.time()-t))

incounted = Counter(indegrees)
counted = Counter(outdegrees)
comcounted = Counter(comdegrees)

insort = sorted(incounted.items(), reverse=True)
sort = sorted(counted.items(), reverse=True)
comsort = sorted(comcounted.items(), reverse=True)


fig = plt.figure()
inax = fig.add_subplot(2,2,1)
ax = fig.add_subplot(2,2,2)
comax = fig.add_subplot(2,2,3)

inline, = inax.plot(*zip(*insort),"*")
line, = ax.plot(*zip(*sort),"*")
comlin, = comax.plot(*zip(*comsort),"*")

inax.set_xscale('log')
inax.set_yscale('log')
inax.set_xlabel("Number of Ingoing TX")
inax.set_ylabel("Number of address")

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Number of outgoing TX")
ax.set_ylabel("Number of address")

comax.set_xscale('log')
comax.set_yscale('log')
comax.set_xlabel("Number of comulated TX")
comax.set_ylabel("Number of address")

#fig = plt.figure()
#ax = fig.add_subplot(2,1,1)

#line, = ax.scatter(*zip(*sort))
#ax.set_yscale('log')
#plt.hist(vert,bins=range(max(vert)+2))
fig.savefig("powerLaw.svg")
print("saves")


for i in tmp_graph.ep.weight.sort():
	print(str(i))

for e in tmp_graph.edges():
	print("weight: "+str(tmp_graph.ep.weight[e]))

for v in tmp_graph.vertices():
	print("address: "+tmp_graph.vp.address[v])

print("motifs:")
graph_tool.clustering.motifs(tmp_graph,1)
print("calculated motifs After: " + str(time.time()-t))

print("motif_significance:")
graph_tool.clustering.motif_significance(tmp_graph,1)
print("calculated motif_significance After: " + str(time.time()-t))

print("local_clustering:")
graph_tool.clustering.local_clustering(tmp_graph)
print("calculated local clustering After: " + str(time.time()-t))

print("local_global_clustering:")
graph_tool.clustering.global_clustering(tmp_graph)
print("calculated global Clustering After: " + str(time.time()-t))

print("extended_clustering:")
graph_tool.clustering.extended_clustering(tmp_graph)
print("calculated extended_clustering After: " + str(time.time()-t))





print("StartHits:")
graph_tool.centrality.hits(tmp_graph)
print("calculated hits After: " + str(time.time()-t))

print("StartEigenvector:")
graph_tool.centrality.eigenvector(tmp_graph)
print("calculated eigenvector After: " + str(time.time()-t))

print("StartPagerank:")
graph_tool.centrality.pagerank(tmp_graph)
print("calculated pagerank After: " + str(time.time()-t))

#print("StartCloseness:")
#graph_tool.centrality.closeness(tmp_graph)
#print("calculated closeness After: " + str(time.time()-t))

#print("betweenness")
#graph_tool.centrality.betweenness(tmp_graph)
#print("calculated betweenness After: " + str(time.time()-t))

#print("StartKatz:")
#graph_tool.centrality.katz(tmp_graph)
#print("calculated katz After: " +str(time.time()-t))
#for address in addresses:
#	print(counter)
#	counter+=1