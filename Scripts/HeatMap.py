import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

#loads in wrapped data
df = pd.DataFrame(np.load("wrapped.npy"))

#use pandas cut to databin based on position
quantiles = 150
labels = list(range(0,quantiles))
print(labels)
df['xcut'] = pd.qcut(df[2],quantiles,labels=labels)
df['ycut'] = pd.qcut(df[3],quantiles,labels=labels)


#sets conditions for z-axis
df = df.loc[(df[4]>0) & (df[4] < 60)].reset_index()
print(df)

#Creates empty numpy array of object data type
arr = np.empty((quantiles,quantiles),dtype=object)
arr2 = np.empty((quantiles,quantiles))
#iterates through each row of the dataframe
for row in df.itertuples():
        #makes the first element of the empty ndarray equal to sqrDisp
        if arr[row[8],row[9]] is not None:
            arr[row[8]][row[9]] = np.append(arr[row[8]][row[9]],row[7])
        #appends if first element is not None
        else:
            arr[row[8],row[9]] = row[7]

#iterates through range of quantiles
for i in range(quantiles):
    #iterates a second time through range of quantiles
    for j in range(quantiles):
        #if there is no stored value in the array sets the value =0
        if (arr[i,j] is None):
            arr[i,j] = 0
        #takes the mean across all sqrDisp stored in that section of the heatmap
        arr2[i,j] = float(np.mean(arr[i,j]))

    
sb.heatmap(arr2)
