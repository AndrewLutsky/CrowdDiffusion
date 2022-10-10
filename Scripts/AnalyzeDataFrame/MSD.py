import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sb
from scipy.optimize import curve_fit

#Reads in dataframe
data3 = pd.read_csv("Dataframe_1.csv")
data3 = data3.dropna()


#Creates data
distProtein = data3['DistFromProtein']
x = data3['nx']
y = data3['ny']
z = data3['nz']
r = np.sqrt(x**2 + y**2 + z**2)
data2 = pd.DataFrame()
data2['r'] = r
data2['DistFromProtein'] = distProtein
print(data2)
sb.scatterplot(data=data2,x="DistFromProtein",y="r")

#numBins = 500
#fig = plt.figure()
#ax = fig.add_subplot(111)
#
#ax.hist(x,numBins,weights = weights, alpha=0.2)
#ax.set_xlabel("Step Size")
#ax.set_ylabel("Count")
#plt.show()
