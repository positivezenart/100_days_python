def add_two_digits(number_value):
    return int(number_value[0]) + int(number_value[1])

number_value = input("enter the number? \n")
print(f"addition of values,{add_two_digits(number_value)}")
