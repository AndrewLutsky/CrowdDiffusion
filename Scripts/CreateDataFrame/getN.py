import pandas as pd
import numpy as np

data = pd.read_csv("Dataframe_.csv")

dx = [None] * len(data['X'])
dy = dx
dz = dx

data = data.sort_values(by = ['Index','Frame Number'])
for i in range(len(data['X'])):
    
    if data['Frame Number'].iloc[i] != 0:
        dx[i] = data['X'].iloc[i] - data['X'].iloc[i-1] 
        dy[i] = data['Y'].iloc[i] - data['Y'].iloc[i-1]
        dz[i] = data['Z'].iloc[i] - data['Z'].iloc[i-1]
    elif i == 1:
         dx[i] = data['X'].iloc[i] - data['X'].iloc[i-1]
         dy[i] = data['Y'].iloc[i] - data['Y'].iloc[i-1]
         dz[i] = data['Z'].iloc[i] - data['Z'].iloc[i-1]
data['nx'] = dx
data['ny'] = dy
data['nz'] = dz

data = data.sort_values(by = ['Frame Number','Index'])
data.to_csv("Dataframe_1.csv")
