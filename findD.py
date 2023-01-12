import numpy as np
import pandas as pd
import seaborn as sb

#loads in wrapped Data
wrapped = pd.DataFrame(np.load("wrapped.npy"))
print(wrapped)
#input time step(ps)
time_step = 5e-12

#Formula for Diffusion coefficient in 3 dimensions is sqrt(6Dt) = MSD

 
#calculate MSD
MSD = wrapped[5].mean()
STD = np.std(wrapped[5])
print("Mean Square Displacement of ion is ... ",MSD, " STD = ",STD)

#Convert MSD to Diffusion Coefficient
MSD = MSD * (10**(-20))
D = MSD/(6*time_step)

print("Diffusion coefficient of Sodium in m^2/second (e-9) : ", D)







