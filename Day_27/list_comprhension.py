number = [1, 2, 3, 4, 5]
number_list = [new_item+1 for new_item in number]
print(number_list)

name = "Mahesh" 

letter_list = [new_item for new_item in name]
print(letter_list)

doubled_numbers = [i+i for i in range(1,6)]
print(doubled_numbers)