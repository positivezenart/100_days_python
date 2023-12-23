import pandas as pd

df = pd.read_csv(f"Day_25\Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df)
print(df["Primary Fur Color"].unique())
#print(df.groupby('Primary Fur Color')["Unique Squirrel ID"].transform('nunique'))



unique_count = df.groupby(['Primary Fur Color'], as_index=False).agg(count=('Unique Squirrel ID','nunique'))

print(unique_count)