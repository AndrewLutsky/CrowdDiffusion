import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
data = pd.read_csv("Dataframe_1.csv")




def getSqrDisplacementFromReference(Index, data):
    indexData = data.where(data['Index'] == Index)
    indexData = indexData.dropna(how='all')
    ref = indexData.where(indexData['Frame Number'] == 0)
    ref = ref.dropna(how = 'all')
    refx = ref['X']
    refy = ref['Y']
    refz = ref['Z']

    r_t = [None] * len(indexData['X'])
    disp = r_t
    for i in range(len(indexData['X'])):
        r_t[i] = np.sqrt((indexData['X'].iloc[i] - ref['X'].iloc[0])**2 + (indexData['Y'].iloc[i] - ref['Y'].iloc[0])**2 + (indexData['Z'].iloc[i] - ref['Z'].iloc[0])**2)
        disp[i] = r_t[i] **2
    return disp

def getDisplacementX(Index,data):
    indexData = data.where(data['Index'] == Index)    
    indexData = indexData.dropna(how='all')    
    ref = indexData.where(indexData['Frame Number'] == 0)    
    ref = ref.dropna(how = 'all')    
    refx = ref['X']    
    refy = ref['Y']    
    refz = ref['Z']    
    
    x_t = [None] * len(indexData['X'])
    for i in range(len(indexData['X'])):
            x_t[i] = (indexData['X'].iloc[i] - ref['X'].iloc[0])**2
    return x_t


slopes = [None] * data['Index'].max()

for i in range(data['Index'].max()):
    y = getSqrDisplacementFromReference(i, data)
    x = np.arange(1,len(y)+1)
    x = x.reshape(-1,1)
    model = LinearRegression(fit_intercept = True).fit(x,y)
    y_pred = model.predict(x)
    slopes[i] = model.coef_


#Print Mean of Slopes
print("Mean of Slopes: ",np.mean(slopes))
print("Std Deviation of Slopes: ",np.std(slopes))
##Graphing the Slopes
#fig = plt.figure()
#ax = fig.add_subplot(111)
#x = [None]*len(slopes)
#for i in range(len(x)):
#    x[i] = slopes[i][0]
#
#x = list(filter(lambda ele:ele is not None, x))
#numBins = 50
#ax.hist(x,numBins,color='lightgreen',alpha=0.8)
#ax.set_xlabel("Slopes")
#ax.set_ylabel("Count")
#plt.show()
