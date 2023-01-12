import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
from sklearn import preprocessing

#Reads in dataframe
data = pd.read_csv("Dataframe_1.csv")
data = data.dropna()


data = data.where(data['Frame Number'] < (230000))
data = data.dropna(how='all')
#Creates data
x = data['nx']
y = data['ny']
z = data['nz']
#x= preprocessing.normalize([x])
#x2 = [None] * len(x[0])
#for i in range(len(x[0])):
#    x2[i] = x[0][i]
#r = np.sqrt(x**2 + y**2 + z**2)
weights = np.ones_like(x)/float(len(x))
print(x)
def gaussian(x, D):
    return (1/((4*np.pi*(D))**(1/2))) * np.exp(-(x**2)/(4*(D)))
#    return (1/(np.sqrt(2*np.pi*(D**2))))*np.exp(-(x**2)/(2*(D**2)))
bin_heights, bin_borders, _ = plt.hist(x,bins = 500, label='histogram',weights = weights,density=True)
bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
popt, _ = curve_fit(gaussian, bin_centers, bin_heights)
x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)
plt.plot(x_interval_for_fit, gaussian(x_interval_for_fit, *popt), label = 'fit')
print(popt)
plt.legend()
plt.show()

#numBins = 500
#fig = plt.figure()
#ax = fig.add_subplot(111)

#ax.hist(x,numBins,weights = weights, alpha=0.2)
#ax.set_xlabel("Step Size")
#ax.set_ylabel("Count")
#plt.show()
