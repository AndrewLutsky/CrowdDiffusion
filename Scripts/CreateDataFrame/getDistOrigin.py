import pandas as pd
import numpy as np

data = pd.read_csv("Dataframe_1.csv")
data = data.sort_values(by = ['Index','Frame Number'])



def getR(index, data):
    data = data.where(data['Index'] == index)
    data = data.dropna(how='all')
    refx = data['X'].where(
            



#    
#    if data['Frame Number'].iloc[i] != 0:
#        dx[i] = data['X'].iloc[i] - data['X'].iloc[i-1] 
#        dy[i] = data['Y'].iloc[i] - data['Y'].iloc[i-1]
#        dz[i] = data['Z'].iloc[i] - data['Z'].iloc[i-1]
#    elif i == 1:
#         dx[i] = data['X'].iloc[i] - data['X'].iloc[i-1]
#         dy[i] = data['Y'].iloc[i] - data['Y'].iloc[i-1]
#         dz[i] = data['Z'].iloc[i] - data['Z'].iloc[i-1]
#data['nx'] = dx
#data['ny'] = dy
#data['nz'] = dz
#
#data = data.sort_values(by = ['Frame Number','Index'])
#data.to_csv("Dataframe_2.csv")
