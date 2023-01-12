import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#create an array with the wrapped box size
pbc_get = [94.830002, 131.889999, 113.828003]

#create the distances to the periodic boundary

pbc_get_dist = np.divide(pbc_get,2)
#create an array with the position of the center of the wrapped unit cell
centercoords = [-1.5856287479400635, 9.305753707885742, -2.9300177097320557]

#enter in time between frames(ns)
time_per_step = 0.01
time_per_step_ins = 0.00000000001
#reads in data(Change data here)
data = pd.read_csv("PosClaFixedStd.csv")
dataProt = pd.read_csv("PosProteinFixedStd.csv")
print(data)
print(dataProt)


#creates DistFromProtein Column for each frame
#gives the distance from the center of the protein
temp = pd.DataFrame()
temp['Frame Number'] = data['Frame Number']
temp['Index'] = data['Index']
temp2 = [None] * len(temp['Index'])
for i in range(len(temp['Index'])):
    tempx = data['X'].iloc[i]
    tempy = data['Y'].iloc[i]
    tempz = data['Z'].iloc[i]
    protx = dataProt['X'].iloc[data['Frame Number'].iloc[i]]
    proty = dataProt['Y'].iloc[data['Frame Number'].iloc[i]]
    protz = dataProt['Z'].iloc[data['Frame Number'].iloc[i]]
    dist = np.sqrt((tempx-protx)**2 + (tempy-proty)**2 + (tempz-protz)**2)
    temp2[i] = dist


data['DistFromProtein'] = temp2
del temp
del temp2
del tempx
del tempy
del tempz
del protx
del protz
del proty
del dist

print(data)
data.to_csv("Dataframe_.csv" )
