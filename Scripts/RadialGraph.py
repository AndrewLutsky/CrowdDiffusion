import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#load in data frame

#load in different ions/systems
dfSod = pd.DataFrame(np.load("wrappedSod.npy"))
dfSod.name = 'Sodium'
dfMag = pd.DataFrame(np.load("wrappedMag.npy"))
dfMag.name = 'Magnesium'
dfClaM = pd.DataFrame(np.load("wrappedClaM.npy"))
dfClaM.name = 'Chloride in Condition B'
dfClaN = pd.DataFrame(np.load("wrappedClaN.npy"))
dfClaN.name = 'Chloride in Condition A'

fig, axes = plt.subplots(1,1)
plt.rcParams['font.weight'] = 'bold'
#delete column indeces and frame numbers because not necessary
for i in [dfSod, dfMag, dfClaN, dfClaM]:
    del i[0]
    del i[1]
    #add new column names
    i.columns = ['X', 'Y', 'Z', 'sqrDisp']
    i['r'] = np.sqrt(np.square(i['X']) + np.square(i['Y']) + np.square(i['Z']))
    
    #finds maximum range of min and max
    rangeR = (i['r'].min(),i['r'].max())
    print(rangeR)
    #bins values together
    bins = np.linspace(0,rangeR[1], int(rangeR[1]))
    group = i.groupby(pd.cut(i['r'],bins))
    plot_centers = (bins [:-1] + bins [1:])/2
    plot_values = group['sqrDisp'].mean() * (10e-20)/(30e-11)
    std_values = group['sqrDisp'].sem() * (10e-20)/(30e-11)
    print(i)
    #create new values
    df = pd.DataFrame()
    

    df['Centers'] = plot_centers
    df['Values'] = plot_values
    df['Std'] = std_values
    df['min'] = plot_values - std_values
    df['max'] = plot_values + std_values
    df = df.fillna(0)
    sb.lineplot(data=df, x='Centers', y='Values',label=i.name, legend = 'full')
    plt.fill_between(x= df['Centers'], y1 = df['min'], y2=df['max'], alpha =0.5)


axes.set_ylabel("Diffusion Coefficient (m\u00b2/s)", fontdict ={"fontweight": "bold"} )
axes.set_xlabel("Radius from Center of Protein (\u212B)", fontdict ={"fontweight": "bold"})
axes.legend()
plt.savefig('RadialGraph.png', dpi = 500)
