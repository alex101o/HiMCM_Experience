import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Untitled_2.csv")
CiC = list(df.iloc[0,:])
AtM = list(df.iloc[1,:])


plt.scatter(CiC,AtM)
plt.xlabel('Percent Change in Carbon Emission')
plt.ylabel('Percent Change in ATM CO2')
plt.title('Percent Change in CiC to AtM')
z = np.polyfit(CiC, AtM, 1)
p = np.poly1d(z)
plt.plot(CiC, p(CiC), color="purple", linewidth=2, linestyle="-")
plt.savefig('CiC_to_AtM_Percent.jpg')