import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

#loads in wrapped data
df = pd.DataFrame(np.load("wrapped.npy"))


#deletes old columns
del df[0]
del df[1]

#adds new column names
df.columns = ['X', 'Y', 'Z', 'sqrDisp']

#use pandas cut to databin based on position


#find range of X values and range of Y value


xrange = (df['X'].min(), df['X'].max())
yrange = (df['Y'].min(), df['Y'].max())
zrange = (df['Z'].min(), df['Z'].max())

xlen = int(xrange[1] - xrange[0])
ylen = int(yrange[1] - yrange[0])
zlen = int(zrange[1] - zrange[0])

print('This simulations is ',xlen,'x',ylen,'x',zlen)

ratio = int(ylen/xlen)
scale = 200

################## Can manually change this otherwise assumes one square angstrom box ##################
#xquantiles = scale
#yquantiles = ratio * scale


xquantiles = 200
yquantiles = 150

#creates labels based on the size of x and y
xlabels = list(range(0,xquantiles))
ylabels = list(range(0,yquantiles))

#cuts using ratio of x to y
df['xcut'] = pd.qcut(df['X'],xquantiles,labels=xlabels)
df['ycut'] = pd.qcut(df['Y'],yquantiles,labels=ylabels)





#sets conditions for z-axis
df = df.loc[(df['Z']>60) & (df['Z'] < 100)].reset_index()
print(df)

#Creates empty numpy array of object data type
arr = np.empty((yquantiles,xquantiles),dtype=object)
arr2 = np.empty((yquantiles,xquantiles))
#iterates through each row of the dataframe
for row in df.itertuples():
        #makes the first element of the empty ndarray equal to sqrDisp
        if arr[row[7],row[6]] is not None:
            arr[row[7]][row[6]] = np.append(arr[row[7]][row[6]],row[5])
        #appends if first element is not None
        else:
            arr[row[7],row[6]] = row[5]

#iterates through range of quantiles
for i in range(yquantiles):
    #iterates a second time through range of quantiles
    for j in range(xquantiles):
        #if there is no stored value in the array sets the value =0
        if (arr[i,j] is None):
            arr[i,j] = 0
        #takes the mean across all sqrDisp stored in that section of the heatmap
        arr2[i,j] = float(np.mean(arr[i,j]))

    
#Creates a heatmap graph
sb.heatmap(arr2)
plt.show()
