import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
dfSod = pd.DataFrame(np.load("wrappedSod.npy"))
dfSod.name = 'Sodium'
dfMag = pd.DataFrame(np.load("wrappedMag.npy"))
dfMag.name = 'Magnesium'
dfClaM = pd.DataFrame(np.load("wrappedClaM.npy"))
dfClaM.name = 'Chloride in Condition B'
dfClaN = pd.DataFrame(np.load("wrappedClaN.npy"))
dfClaN.name = 'Chloride in Condition A'


fig, axes = plt.subplots(1,1)
#plt.figure(figsize=(10,8))
plt.rcParams['font.weight'] = 'bold'
maxr = 0
for i in [dfSod, dfMag, dfClaM, dfClaN]:
    del i[0]
    del i[1]
    
    i.columns = ['X', 'Y', 'Z', 'sqrDisp']
    i['r'] = np.sqrt(np.square(i['X']) + np.square(i['Y']) + np.square(i['Z']))
    i['D'] = i['sqrDisp'] * (10e-20)/(30e-11)
    if maxr < i['r'].max():
        maxr = i['r'].max()
    print(i)
    #finds maximum range of min and max
    #rangeR = (i['r'].min(),i['r'].max())
    axes = sb.kdeplot(i, x='r', label = i.name )
plt.xlim(0, 50)
axes.legend(loc="upper center", fancybox = True, bbox_to_anchor = (0.5,1.35))
axes.set_ylabel("Relative Density", fontdict={"fontweight":"bold"})
axes.set_xlabel("Radius (\u212B)", fontdict ={"fontweight": "bold"})
plt.tight_layout()
plt.savefig('RDF.png', dpi=500)
#plt.show()
