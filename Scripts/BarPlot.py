import seaborn as sb
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
vals = [1.29e-9, 1.89e-9, 2.91e-9, 2.77e-9, 1.22e-9, 1.77e-9, 2.89e-9, 2.72e-9] 
sem = [0.00086, 0.00196, 0.00088,0.00148, 0.00084, 0.00179, 0.00074, 0.00134]

    
    
plt.figure(figsize=(14,8))
ions = ['Magnesium', 'Sodium', 'Chloride Condition A','Chloride Condition B', 'Magnesium', 'Sodium', 'Chloride Condition A', 'Chloride Condition B']
condn = ['Not Crowded', 'Not Crowded', 'Not Crowded','Not Crowded', 'Crowded','Crowded', 'Crowded', 'Crowded']
dict = {'vals':vals, 'sem':sem, 'ions':ions, 'condn':condn}
df = pd.DataFrame(dict)

print(df)
g = sb.barplot(data=df,x='ions',y='vals',hue='condn',palette = 'dark', alpha = 0.55)
g.set(ylabel = "Diffusion Coefficient (m\u00B2/s) \n")
plt.legend(bbox_to_anchor=(1.05, 0.5), loc=2, frameon = False)
plt.savefig("BarPlotFig1.png",bbox_inches = 'tight',dpi=300)

