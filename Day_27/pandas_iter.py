import pandas as pd
student_dict ={
    "student":["Anglea","Mahesh","Ramu"],
    "score" :[50,60,70]
}

df = pd.DataFrame(student_dict)
print(df)

for index,row in df.iterrows():
    print(row)
