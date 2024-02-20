import pandas as pd 
df =pd.read_csv("Day_25\weather_data.csv")
df_dict =df.to_dict()
print(df_dict)
df_list =df['temp'].to_list()
print(df_list)

print(df['temp'].mean())
print(df['temp'].agg('max'))

#get data in columns

print(df[df.day == "Monday"])

print(df.iloc[0:2])

print(df[df.temp == df.temp.agg('max')])

monday = df[df.day == "Monday"]
faranheit = (1.8 * monday.temp) + 32
print(f"{monday.day} temperatur ins faranheit is {faranheit}")