import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from math import e

# Open CSV
Raw_GVDF = pd.read_csv("Gamma_Values/Pure_Excel_Gamma_Values_Data.csv")

# Get Raw
Act_PPM = Raw_GVDF.iloc[:,1]
Act_PPM = list(Act_PPM)
Years = Raw_GVDF.iloc[:,0]
Years = list(Years)

# Get Constants Values
UI = Raw_GVDF.iloc[0,3]
UG = Raw_GVDF.iloc[1,3]
R0 = Raw_GVDF.iloc[2,3]
Ri = Raw_GVDF.iloc[3,3]
Range = 1400

# Creating Lists of Inputs
Gamma_List = []
Input_List = []
r_squared_list = []
coef_list = []
inter_list = []
Input_CSV = pd.DataFrame()
r_squared_df = pd.DataFrame()

# List of X Inputs
for ii in range(len(Years)):
    temp = -1 + e**((UG+UI)*(ii+1))
    Input_List.append(temp)
Input_CSV["X_Inputs"] = Input_List


# List of Gamma Inputs
for ii in range(Range-1):
    R0 = Ri * (ii+1)
    # R0 = R0 // 0.01 *0.01
    Gamma_List.append(R0)
    
# Model
model = LinearRegression()

# Procedure
for ii in Gamma_List:
    temp_list = []
    for iii in range(len(Act_PPM)):
        temp = Act_PPM[iii]**ii
        temp_list.append(temp)
    Input_CSV["Act_Y"] = temp_list
    X, y = Input_CSV[["X_Inputs"]], Input_CSV["Act_Y"]
    model.fit(X, y)
    
    
    r_squared = model.score(X, y)
    r_squared_list.append(r_squared)
    
    coeffifience = model.coef_
    inter = model.intercept_
    coef_list.append(coeffifience)
    inter_list.append(inter)
r_squared_df["Gamma_Values"] = Gamma_List
r_squared_df["R_Squared_Values"] = r_squared_list
r_squared_df["Coef"] = coef_list
r_squared_df["intercepts"] = inter_list
print(r_squared_df.max())
r_squared_df.to_csv("Gamma_Values/R_Squared_Values.csv", index=False)
