import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

plt.figure()
plt.stackplot(range(1999,2009),[[0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333],[0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333],[0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333,0.33333]], 
          colors=['#FFFF00','#FF0000','#000000'])
plt.xlim(1999,2008)

plt.legend([mpatches.Patch(color='#000000'),  
            mpatches.Patch(color='#FF0000'), 
            mpatches.Patch(color='#FFFF00')], 
           ['amount of black in german flag','amount of red in german flag','amount of yellow in german flag'])

plt.savefig("stacked.svg")


#   https://python-graph-gallery.com/255-percentage-stacked-area-chart/