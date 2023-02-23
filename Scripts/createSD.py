import numpy as np
import pandas as pd

#reads in wrapped and unwrapped positional data - this data can be any positional 
# and time series data described in the readme, but needs both wrapped and unwrapped
unwrapped = pd.read_csv('PosMagUnwrapped.csv')
wrapped = pd.read_csv('PosMagWrapped.csv')


#finds the maximum frame number - wrapped and unwrapped should be same length
maxFrame = unwrapped['Frame Number'].max()

#sorts by index number
unwrapped = unwrapped.sort_values(by=['Index','Frame Number'])
wrapped = wrapped.sort_values(by=['Index','Frame Number'])


#writes empty numpy arrays
dXFin = np.array([])
dYFin = np.array([])
dZFin = np.array([])


#loops through unique values in the Index Column
for i in unwrapped.Index.unique(): 
    
    #slices through unwrapped dataframe
    indexDF = unwrapped.loc[unwrapped['Index'] == i]
    
    #stores change in X,Y,Z
    dX = np.diff(indexDF['X'])
    dY = np.diff(indexDF['Y'])
    dZ = np.diff(indexDF['Z'])
    
    #inserts 0 value at beginning of array to match lengths
    dX = np.insert(dX, 0, 0)
    dY = np.insert(dY, 0, 0)
    dZ = np.insert(dZ, 0, 0)
    
    #concatenates index list of change in positions to final column
    dXFin = np.concatenate([dXFin, dX])
    dYFin = np.concatenate([dYFin, dY])
    dZFin = np.concatenate([dZFin, dZ])

#adds each column to the dataframe
unwrapped['dX'] = dXFin
unwrapped['dZ'] = dZFin
unwrapped['dY'] = dYFin

#creates a column for square change in X,Y, and Z
unwrapped['dX2'] = np.square(unwrapped['dX'])
unwrapped['dY2'] = np.square(unwrapped['dY'])
unwrapped['dZ2'] = np.square(unwrapped['dZ'])

#calculate sqrDisp
unwrapped['sqrDisp'] = unwrapped['dX2'] + unwrapped['dY2'] + unwrapped['dZ2']

#add sqrDisp to wrappedData
wrapped['sqrDisp'] = unwrapped['sqrDisp']


#still needs to be processed (remove the first, second and last frame number data)
badValues = [0,1,maxFrame]
unwrapped = unwrapped[~unwrapped['Frame Number'].isin(badValues)]
wrapped = wrapped[~wrapped['Frame Number'].isin(badValues)]


#saves as numpy array
unwrapped = unwrapped.to_numpy()
wrapped = wrapped.to_numpy()
np.save("unwrapped",unwrapped)
np.save("wrapped",wrapped)
