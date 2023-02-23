import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import matplotlib.colors

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 24
plt.rcParams['font.weight'] = 'bold'
#loads in wrapped data
df = pd.DataFrame(np.load("wrapped.npy"))

print("loaded in")

#deletes old columns
del df[0]
del df[1]

df = df.dropna()


#adds new column names
df.columns = ['X', 'Y', 'Z', 'sqrDisp']

#sets the other dataframes
dfX = df
dfY = df

#find range of X Y and Z values


xrange = (df['X'].min(), df['X'].max())
yrange = (df['Y'].min(), df['Y'].max())
zrange = (df['Z'].min(), df['Z'].max())
sqrDispRange = (df['sqrDisp'].min(), df['sqrDisp'].max())
xlen = int(xrange[1] - xrange[0])
ylen = int(yrange[1] - yrange[0])
zlen = int(zrange[1] - zrange[0])
print(xrange,yrange,zrange, sqrDispRange)
print('This simulations is ',xlen,'x',ylen,'x',zlen)
sqrDispMax = (df['sqrDisp'].max())







#Restrict X, Y, and Z for YX Heatmap

Zrestrict = 10
Xrestrict = 40
Yrestrict = 40
df = df.loc[(df['Z']>-Zrestrict) & (df['Z'] < Zrestrict)].reset_index()
df = df.loc[(df['X']>-Xrestrict) & (df['X'] < Xrestrict)].reset_index()
df = df.loc[(df['Y']>-Yrestrict) & (df['Y'] < Yrestrict)]

#Restrict X,Y, and Z for ZY Heatmap


Zrestrict = 40
Xrestrict = 10
Yrestrict = 40
dfX = dfX.loc[(dfX['Z']>-Zrestrict) & (dfX['Z'] < Zrestrict)].reset_index()
dfX = dfX.loc[(dfX['X']>-Xrestrict) & (dfX['X'] < Xrestrict)].reset_index()
dfX = dfX.loc[(dfX['Y']>-Yrestrict) & (dfX['Y'] < Yrestrict)]

#Restrict X,Y, and Z for ZX Heatmap

Zrestrict = 40
Xrestrict = 40
Yrestrict = 10
dfY = dfY.loc[(dfY['Z']>-Zrestrict) & (dfY['Z'] < Zrestrict)].reset_index()
dfY = dfY.loc[(dfY['X']>-Xrestrict) & (dfY['X'] < Xrestrict)].reset_index()
dfY = dfY.loc[(dfY['Y']>-Yrestrict) & (dfY['Y'] < Yrestrict)]


#determine number of bins
xquantiles = 40
yquantiles = 40
zquantiles = 40

#creates labels based on the size of x and y
xlabels = list(range(0,xquantiles))
ylabels = list(range(0,yquantiles))
zlabels = list(range(0,zquantiles))


#Cut each dataframe into X Y and Z
df['xcut'] = pd.cut(df['X'],xquantiles,labels=xlabels)
df['ycut'] = pd.cut(df['Y'],yquantiles,labels=ylabels)
df['zcut'] = pd.cut(df['Z'],zquantiles, labels=zlabels)
dfX['xcut'] = pd.cut(dfX['X'],xquantiles,labels=xlabels)
dfX['ycut'] = pd.cut(dfX['Y'],yquantiles,labels=ylabels)
dfX['zcut'] = pd.cut(dfX['Z'],zquantiles, labels=zlabels)
dfY['xcut'] = pd.cut(dfY['X'],xquantiles, labels=zlabels)
dfY['ycut'] = pd.cut(dfY['Y'],yquantiles,labels=ylabels)
dfY['zcut'] = pd.cut(dfY['Z'],zquantiles, labels=zlabels)
del df['level_0']
del dfX['level_0']
del dfY['level_0']

#CREATE YX HEATMAP
arrYX = np.empty((yquantiles,xquantiles),dtype=object)
arr2YX = np.empty((yquantiles,xquantiles))

for row in df.itertuples():
        #makes the first element of the empty ndarrYXay equal to sqrDisp
        if arrYX[int(row[7]),int(row[6])] is not None:
            arrYX[int(row[7])][int(row[6])] = np.append(arrYX[int(row[7])][int(row[6])],row[5])
        #appends if first element is not None
        else:
            arrYX[int(row[7]),int(row[6])] = row[5]


#CREATE ZY HEATMAP
arrZY = np.empty((zquantiles,yquantiles),dtype = object)
arr2ZY = np.empty((zquantiles,yquantiles))
for row in dfX.itertuples():
        #makes the first element of the empty ndarrZYay equal to sqrDisp
        if arrZY[int(row[8]),int(row[7])] is not None:
            arrZY[int(row[8])][int(row[7])] = np.append(arrZY[int(row[8])][int(row[7])],row[5])
        #appends if first element is not None
        else:
            arrZY[int(row[8]),int(row[7])] = row[5]


#CREATE ZX HEATMAP
arrZX = np.empty((zquantiles,xquantiles),dtype = object)
arr2ZX = np.empty((zquantiles,xquantiles))
for row in dfY.itertuples():
        #makes the first element of the empty ndarrZXay equal to sqrDisp
        if arrZX[int(row[8]),int(row[6])] is not None:
            arrZX[int(row[8])][int(row[6])] = np.append(arrZX[int(row[8])][int(row[6])],row[5])
        #appends if first element is not None
        else:
            arrZX[int(row[8]),int(row[6])] = row[5]

#iterates through range of quantiles
for i in range(yquantiles):
    #iterates a second time through range of quantiles
    for j in range(xquantiles):
        #if there is no stored value in the array sets the value =0
        if (arrZX[i,j] is None):
            arrZX[i,j] = 0
        if (arrYX[i,j] is None):
            arrYX[i,j] = 0
        if (arrZY[i,j] is None):
            arrZY[i,j] = 0
        #takes the mean across all sqrDisp stored in that section of the heatmap
        arr2ZX[i,j] = float((np.mean(arrZX[i,j])/(6*5e-12)) * (10e-21))
        arr2YX[i,j] = float((np.mean(arrYX[i,j])/(6*5e-12)) * (10e-21))
        arr2ZY[i,j] = float((np.mean(arrZY[i,j])/(6*5e-12)) * (10e-21))
print(arr2ZX)    
#Creates a heatmap graph

#####createSeaborn HeatMap####




arr2YZ = np.flip(arr2ZY, axis = 0)
arr2ZX = np.flip(arr2ZX, axis = 0)
arr2YX = np.flip(arr2YX, axis = 0)
fig, (ax1, ax2, ax3, axcb) = plt.subplots(1,4, figsize=(20,6), gridspec_kw = {'width_ratios':[1,1,1,0.05]})
g1 = sb.heatmap(arr2YX, vmin = 0,vmax = 30e-10,cbar = False, robust= True, ax=ax1, cmap='Blues')
g2 = sb.heatmap(arr2ZY, vmin = 0, vmax = 30e-10,cbar = False, robust= True, ax=ax2, cmap='Blues')
g3 = sb.heatmap(arr2ZX, vmin = 0,vmax = 30e-10,cbar = True,cbar_ax=axcb, robust= True,ax=ax3, cmap='Blues')

#set colorbar label
axcb.set_ylabel("Diffusion Coefficient(m\u00B2/s)", fontweight = "bold", labelpad = 20)

#set tick labels
for i in [g1,g2,g3]:
    i.set_xticks([0.5,9.5,19.5,29.5,39.5])
    i.set_xticklabels(["-40","-20", "0","20", "40"])
    i.set_yticks([39.5,29.5,19.5,9.5,0.5])
    i.set_yticklabels(["-40","-20", "0","20","40"])


#Setting axes titles and labels - bolded font
ax1.set_title("YX", fontdict = {"fontweight": "bold"})
ax1.set_xlabel("X position", fontdict = {"fontweight": "bold"})
ax1.set_ylabel("Y position", fontdict = {"fontweight": "bold"})

ax2.set_title("ZY", fontdict = {"fontweight": "bold"})
ax2.set_xlabel("Y position", fontdict = {"fontweight": "bold"})
ax2.set_ylabel("Z position", fontdict = {"fontweight": "bold"})
ax3.set_title("ZX", fontdict = {"fontweight": "bold"})
ax3.set_xlabel("X position", fontdict = {"fontweight": "bold"})
ax3.set_ylabel("Z position", fontdict = {"fontweight": "bold"})
plt.tight_layout()

#Saves thef figure in question
plt.savefig('ClaMHM.png', dpi = 500)
