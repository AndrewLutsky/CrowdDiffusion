import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#load in data frame
df = pd.DataFrame(np.load("wrapped.npy"))
#delete column indeces and frame numbers because not necessary
del df[0]
del df[1]
#add new column names

df.columns = ['X', 'Y', 'Z', 'sqrDisp']
#print out dataframe
print(df)
df = df


df['r'] = np.sqrt(np.square(df['X']) + np.square(df['Y']) + np.square(df['Z']))
rangeR = (df['r'].min(),df['r'].max())
print(rangeR)
bins = np.linspace(rangeR[0],rangeR[1], int(rangeR[1]-rangeR[0]))
group = df.groupby(pd.cut(df['r'],bins))
plot_centers = (bins [:-1] + bins [1:])/2
plot_values = group['sqrDisp'].mean()
std_values = group['sqrDisp'].sem()

dfSeaborn = pd.DataFrame()
dfSeaborn['Centers'] = plot_centers
dfSeaborn['Values'] = plot_values
dfSeaborn['Std'] = std_values
dfSeaborn['min'] = plot_values - std_values
dfSeaborn['max'] = plot_values + std_values
dfSeaborn = dfSeaborn.fillna(0)
print(dfSeaborn)


sb.lineplot(data= dfSeaborn, x='Centers', y='Values')
plt.fill_between(x = dfSeaborn['Centers'], y1 = dfSeaborn['min'], y2= dfSeaborn['max'], alpha = 0.5)
#sb.lineplot(data = dfSeaborn, x = "Centers", y= "Std")


plt.show()
