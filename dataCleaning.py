import pandas as pd
import csv
df = pd.read_csv("total_stars.csv")
print(df.shape)
print(df.columns)

#axis 1 = column, axis 2 = row, inplace just confirms we want to drop these columns
df.drop(["Unnamed: 0", "Luminosity", "Unnamed: 6", "Star_name.1", "Distance.1", "Mass.1", "Radius.1"], 
        axis=1, inplace=True)
print(df.shape)
print(df.columns)

finalData = df.dropna()

df.to_csv("FinalizedFile.csv")

print(df.describe)