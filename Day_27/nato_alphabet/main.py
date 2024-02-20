import pandas as pd
"""create a phonetic key of words """
df = pd.read_csv(f"Day_27\\nato_alphabet\\nato_phonetic_alphabet.csv")

dict_phonetic ={row.letter:row.code for index,row in df.iterrows()}
#print(dict_phonetic)

user_input = list(input("Enter a word?"))

phonetic_code = {letter:dict_phonetic[letter.upper()] for letter in user_input}
print(phonetic_code)


