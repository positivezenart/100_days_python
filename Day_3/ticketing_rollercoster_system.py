height = int(input("Please enter the height in centi meters \n"))

if height > 120:
    print("you can ride the wheel")
    bill = 0
    age = int(input("Please enter your age: \n"))
    if age < 12:
        bill += 5
    elif age >12 and age < 18:
        bill += 7
    else:
        bill += 12
    answer =input('do you want photos?(yes|no) \n')
    if answer == 'yes':
        bill += 3
    print(f"the total bill is {bill}")
else:
    print("you cannot ride the wheel")