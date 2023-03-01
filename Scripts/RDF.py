import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
dfSod = pd.DataFrame(np.load("wrappedSod.npy"))
dfSod.name = 'Sodium in NaCl'
dfMag = pd.DataFrame(np.load("wrappedMag.npy"))
dfMag.name = 'Magnesium MgCl\u2082'
dfClaM = pd.DataFrame(np.load("wrappedClaM.npy"))
dfClaM.name = 'Chloride in MgCl\u2082'
dfClaN = pd.DataFrame(np.load("wrappedClaN.npy"))
dfClaN.name = 'Chloride in NaCl'


fig, axes = plt.subplots(1,1)
plt.rcParams['font.weight'] = 'bold'
maxr = 0
for i in [dfSod, dfMag, dfClaN, dfClaM]:
    del i[0]
    del i[1]
    
    i.columns = ['X', 'Y', 'Z', 'sqrDisp']
    i['r'] = np.sqrt(np.square(i['X']) + np.square(i['Y']) + np.square(i['Z']))
    i['D'] = i['sqrDisp'] * (10e-20)/(30e-11)
    if maxr < i['r'].max():
        maxr = i['r'].max()
    #finds maximum range of min and max
    #rangeR = (i['r'].min(),i['r'].max())
    axes = sb.kdeplot(i, x='r', label = i.name )
    x = axes.lines[-1].get_xdata()
    print(axes.lines[-1].get_ydata())
    upper = axes.lines[-1].get_ydata() + i['D'].std()
    lower = axes.lines[-1].get_ydata() - i['D'].std()
    print(x)
    print(upper)
    print(lower)

axes.fill_between(x, lower, upper)

plt.xlim(0, 50)
axes.legend(loc="upper center", fancybox = True, bbox_to_anchor = (0.5,1.35))
axes.set_ylabel("Relative Density", fontdict={"fontweight":"bold"})
axes.set_xlabel("Radius (\u212B)", fontdict ={"fontweight": "bold"})
plt.tight_layout()
plt.savefig('RDFSEM.png', dpi=500)
#plt.show()
