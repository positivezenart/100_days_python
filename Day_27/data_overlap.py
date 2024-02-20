with open("Day_27\\file1.txt", mode='r') as f:
    read_file1 = f.readlines()
with open("Day_27\\file2.txt", mode='r') as f:
    read_file2 = f.readlines()
list_of_int_file1 = [int(num) for num in read_file1 if num != "" and num != '\n']
list_of_int_file2 = [int(num) for num in read_file2 if num != "" and num != '\n']

#mutual_values=[entry for x in list_of_int_file1 for entry in list_of_int_file2 if x in entry]
print(list_of_int_file1)
print(list_of_int_file2)

mutual_values =[i for i in set(list_of_int_file1) if i in list_of_int_file2]
print(mutual_values)






