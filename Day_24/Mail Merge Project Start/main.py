"" "Mail Merge code"""

with open(r"Day_24\Mail Merge Project Start\Input\Names\invited_names.txt",mode ='r') as name:
    names = name.read()

input=names .replace('\n',',')

def Convert(string):
    li = list(string.split(","))
    return li

list_of_names =Convert(input)
for i in list_of_names: 
   item =str(i)
   with open("Day_24\Mail Merge Project Start\Input\Letters\starting_letter.txt",mode='r') as letter:
     letter_text = letter.readlines()
   new_string=letter_text[0].replace("[name]",item)
   letter_text[0] = new_string
   letter_text = " ".join(map(str,letter_text))
   with open(f"Day_24\Mail Merge Project Start\Output\ReadyToSend\letter_{item}.txt",mode ='w') as f:
       f.write(letter_text)
