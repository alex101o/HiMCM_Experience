import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Untitled_3.csv")
CiC = list(df.iloc[0,:])
AtM = list(df.iloc[1,:])

plt.scatter(CiC,AtM)
plt.xlabel('Carbon Emission')
plt.ylabel('Change in ATM CO2')
plt.title('CiC to AtM')
z = np.polyfit(CiC, AtM, 1)
p = np.poly1d(z)
plt.plot(CiC, p(CiC), color="purple", linewidth=2, linestyle="-")
plt.annotate(f"y = {z[0]}x + z{1}", (0, 1))
print(z)
plt.savefig('CE_to_AtM_.jpg')
print(z)