import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

#loads in wrapped data to 3 different data frames
dfWrappedListYX = []
for i in range(1,9):
    stri = str(i)
    fileName = "wrappedAP" + stri + ".npy"
    df = pd.DataFrame(np.load(fileName))
    
    #deletes old columns and removes NaN values
    del df[0]
    del df[1]
    df = df.dropna()
    #adds new column names
    df.columns = ['X', 'Y', 'Z', 'sqrDisp']
    #appends df to a list
    dfWrappedListYX.append(df)

dfWrappedListZY = dfWrappedListYX.copy()
dfWrappedListZX = dfWrappedListYX.copy()


#Restrict X, Y, and Z for YX

Zrestrict = 10
Xrestrict = 40
Yrestrict = 40
for i in range(0,8):
    dfrestrictZ = dfWrappedListYX[i]
    dfrestrictZ = dfrestrictZ.loc[(dfrestrictZ['Z']>-Zrestrict) & (dfrestrictZ['Z'] < Zrestrict)]
    dfrestrictZ = dfrestrictZ.loc[(dfrestrictZ['X']>-Xrestrict) & (dfrestrictZ['X'] < Xrestrict)]
    dfrestrictZ = dfrestrictZ.loc[(dfrestrictZ['Y']>-Yrestrict) & (dfrestrictZ['Y'] < Yrestrict)]
    dfWrappedListYX[i] = dfrestrictZ.reset_index(drop=True)
    del dfrestrictZ



#Restrict X, Y, and Z for ZY
Zrestrict = 40
Xrestrict = 10
Yrestrict = 40

for i in range(0,8):
    dfrestrictX = dfWrappedListZY[i]
    dfrestrictX = dfrestrictX.loc[(dfrestrictX['Z']>-Zrestrict) & (dfrestrictX['Z'] < Zrestrict)]
    dfrestrictX = dfrestrictX.loc[(dfrestrictX['X']>-Xrestrict) & (dfrestrictX['X'] < Xrestrict)]
    dfrestrictX = dfrestrictX.loc[(dfrestrictX['Y']>-Yrestrict) & (dfrestrictX['Y'] < Yrestrict)]
    dfWrappedListZY[i] = dfrestrictX.reset_index(drop=True)
    del dfrestrictX
#Restrict X, Y, and Z for ZX
Zrestrict = 40
Xrestrict = 40
Yrestrict = 5

for i in range(0,8):
    dfrestrictY = dfWrappedListZX[i]
    dfrestrictY = dfrestrictY.loc[(dfrestrictY['Z']>-Zrestrict) & (dfrestrictY['Z'] < Zrestrict)]
    dfrestrictY = dfrestrictY.loc[(dfrestrictY['X']>-Xrestrict) & (dfrestrictY['X'] < Xrestrict)]
    dfrestrictY = dfrestrictY.loc[(dfrestrictY['Y']>-Yrestrict) & (dfrestrictY['Y'] < Yrestrict)]
    dfWrappedListZX[i] = dfrestrictY.reset_index(drop=True)
    del dfrestrictY


#This is the number of bins required
zquantiles = 40
xquantiles = 40
yquantiles = 40

#creates labels based on the size of x and y
xlabels = list(range(0,xquantiles))
ylabels = list(range(0,yquantiles))
zlabels = list(range(0,zquantiles))

#bins the data using pd.cut

for i in range(0,8):
    dfcutYX = dfWrappedListYX[i]
    dfcutYX['xcut'] = pd.cut(dfcutYX['X'],xquantiles,labels=xlabels)
    dfcutYX['ycut'] = pd.cut(dfcutYX['Y'],yquantiles,labels=ylabels)
    #del dfcutYX['level_0']
    dfWrappedListYX[i] = dfcutYX

for i in range(0,8): 
    dfcutZY = dfWrappedListZY[i]
    dfcutZY['ycut'] = pd.cut(dfcutZY['Y'],yquantiles,labels=ylabels)
    dfcutZY['zcut'] = pd.cut(dfcutZY['Z'],zquantiles,labels=zlabels)
    #del dfcutZY['level_0']
    dfWrappedListZY[i] = dfcutZY

for i in range(0,8):
    dfcutZX = dfWrappedListZX[i]
    dfcutZX['xcut'] = pd.cut(dfcutZX['X'],xquantiles,labels=xlabels)
    dfcutZX['zcut'] = pd.cut(dfcutZX['Z'],zquantiles,labels=zlabels)
    #del dfcutZX['level_0']
    dfWrappedListZX[i] = dfcutZX


#Creates empty numpy array of object data type
arrListYX = []
arrListZY = []
arrListZX = []
#uses different for loops because if quantiles size is different
for i in range(0,8):
    arr = np.empty((yquantiles,xquantiles),dtype=object)
    arrListYX.append(arr)
for i in range(0,8):
    arr = np.empty((zquantiles,yquantiles),dtype=object)
    arrListZY.append(arr)
for i in range(0,8):
    arr = np.empty((zquantiles,xquantiles),dtype=object)
    arrListZX.append(arr)



#creates another empty numpy array to store mean values

arr2YX = np.empty((yquantiles,xquantiles))
arr2ZY = np.empty((zquantiles,yquantiles))
arr2ZX = np.empty((zquantiles,xquantiles))


#iterates through each row of the dataframe
for j in range(0,8):
    arr = arrListYX[j]
    df = dfWrappedListYX[j]
    for row in df.itertuples():
            #makes the first element of the empty ndarray equal to sqrDisp
            if arr[int(row[6]),int(row[5])] is not None:
                 arr[int(row[6])][int(row[5])] = np.append(arr[int(row[6])][int(row[5])],row[4])
            #appends if first element is not None
            else:
                arr[int(row[6]),int(row[5])] = row[4]
    arrListYX[j] = arr
for j in range(0,8):
    arr = arrListZY[j]
    dfX = dfWrappedListZY[j]
    print(dfX)
    for row in dfX.itertuples():
            #makes the first element of the empty ndarray equal to sqrDisp
            if arr[int(row[6]),int(row[5])] is not None:
                 arr[int(row[6])][int(row[5])] = np.append(arr[int(row[6])][int(row[5])],row[4])
            #appends if first element is not None
            else:
                arr[int(row[6]),int(row[5])] = row[4]
    arrListZY[j] = arr

for j in range(0,8):
    arr = arrListZX[j]
    dfY = dfWrappedListZX[j]
    for row in dfY.itertuples():
            #makes the first element of the empty ndarray equal to sqrDisp
            if arr[int(row[6]),int(row[5])] is not None:
                 arr[int(row[6])][int(row[5])] = np.append(arr[int(row[6])][int(row[5])],row[4])
            #appends if first element is not None
            else:
                arr[int(row[6]),int(row[5])] = row[4]
    arrListZX[j] = arr





#iterates through list of arrays
arrYX = np.empty((yquantiles,xquantiles),dtype=object)
arrZY = np.empty((zquantiles,yquantiles),dtype=object)
arrZX = np.empty((zquantiles,xquantiles),dtype=object)
  
for i in arrListYX:
    for j in range(yquantiles):
        for k in range(xquantiles):
            
            if arrYX[j,k] is None:
                arrYX[j,k] = i[j,k]
            else:
                if i[j,k] is not None:
                    arrYX[j,k] = np.append(arrYX[j,k], i[j,k])


for i in arrListZY:
    for j in range(zquantiles):
        for k in range(yquantiles):
            print(i[j,k])
            if arrZY[j,k] is None:
                arrZY[j,k] = i[j,k]
            else:
                if i[j,k] is not None:
                    arrZY[j,k] = np.append(arrZY[j,k], i[j,k])


for i in arrListZX:
    for j in range(zquantiles):
        for k in range(xquantiles):
            if arrZX[j,k] is None:
                arrZX[j,k] = i[j,k]
            else:
                if i[j,k] is not None:
                    arrZX[j,k] = np.append(arrZX[j,k], i[j,k])

#iterates through range of quantiles
for i in range(yquantiles):
    #iterates a second time through range of quantiles
    for j in range(xquantiles):
        #if there is no stored value in the array sets the value =0
        if (arrYX[i,j] is None):
            arrYX[i,j] = 0
        #takes the mean across all sqrDisp stored in that section of the heatmap`
        arr2YX[i,j] = float(np.mean(arrYX[i,j]) * (1e-20)/(30e-12))
for i in range(zquantiles):
    #iterates a second time through range of quantiles
    for j in range(yquantiles):
        #if there is no stored value in the array sets the value =0
        if (arrZY[i,j] is None):
            arrZY[i,j] = 0
        #takes the mean across all sqrDisp stored in that section of the heatmap
        arr2ZY[i,j] = float(np.mean(arrZY[i,j])* (1e-20)/(30e-12))

for i in range(zquantiles):
    #iterates a second time through range of quantiles
    for j in range(xquantiles):
        #if there is no stored value in the array sets the value =0
        if (arrZX[i,j] is None):
            arrZX[i,j] = 0
        #takes the mean across all sqrDisp stored in that section of the heatmap
        arr2ZX[i,j] = float(np.mean(arrZX[i,j])* (1e-20)/(30e-12))

print(arr2YX)
print(arr2ZY)    
#Creates a heatmap graph

#createSeaborn HeatMap
arr2YX = np.flip(arr2YX, axis =0)
arr2ZY = np.flip(arr2ZY, axis = 0)
arr2ZX = np.flip(arr2ZX, axis = 0)
#create xticks
#xticks = range(-Xrestrict,Xrestrict,4)
#yticks = range(-Yrestrict,Yrestrict,4)
#print(xticks)
fig, (ax1, ax2, ax3, axcb) = plt.subplots(1,4, figsize=(20,6), gridspec_kw = {'width_ratios':[1,1,1,0.05]})
g1 = sb.heatmap(arr2YX, vmin = 0,cbar = False, robust= True, ax=ax1, cmap='Blues')
g2 = sb.heatmap(arr2ZY, vmin = 0,cbar = False, robust= True, ax=ax2, cmap='Blues')
g3 = sb.heatmap(arr2ZX, vmin = 0,cbar = True,cbar_ax=axcb, robust= True,ax=ax3, cmap='Blues')

axcb.set_ylabel("Diffusion Coefficient(m\u00B2/s)", fontweight = "bold", labelpad = 20)
for i in [g1,g2,g3]:
    i.set_xticks([0.5,9.5,19.5,29.5,39.5])
    i.set_xticklabels(["-40","-20", "0","20", "40"])
    i.set_yticks([39.5,29.5,19.5,9.5,0.5])
    i.set_yticklabels(["-40","-20", "0","20","40"])
ax1.set_title("YX", fontdict = {"fontweight": "bold"})
ax1.set_xlabel("X position", fontdict = {"fontweight": "bold"})
ax1.set_ylabel("Y position", fontdict = {"fontweight": "bold"})

ax2.set_title("ZY", fontdict = {"fontweight": "bold"})
ax2.set_xlabel("Y position", fontdict = {"fontweight": "bold"})
ax2.set_ylabel("Z position", fontdict = {"fontweight": "bold"})
ax3.set_title("ZX", fontdict = {"fontweight": "bold"})
ax3.set_xlabel("X position", fontdict = {"fontweight": "bold"})
ax3.set_ylabel("Z position", fontdict = {"fontweight": "bold"})
axcb.set
#ax.set(xlabel="x position", ylabel="y position" )
plt.tight_layout()
plt.savefig('MagHM2N.png',dpi=500)
