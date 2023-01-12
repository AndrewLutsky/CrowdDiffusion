import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


def probability(x, a, b,c):
    #return amplitude * np.exp( - (x - mean)**2 / (2*standard_deviation ** 2))
    return (((3/(2*np.pi))*(x**2)/(6*b*c)))**(3/2) * np.exp(-(a**2)/(6*b*c) )    

#Reads in dataframe
data = pd.read_csv("Dataframe_1.csv")
data = data.dropna() 
#Creates data
x = data['nx']
y = data['ny']
z = data['nz']
r = np.sqrt((x**2) + (y**2) + (z**2))
r2 = r**2


bin_heights, bin_borders, _ = plt.hist(r, bins='auto', label='histogram')
bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
popt, _ = curve_fit(probability, bin_centers, bin_heights)

x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)
print(popt)
plt.plot(x_interval_for_fit, probability(x_interval_for_fit, *popt), label='fit')
plt.legend()
plt.show()
