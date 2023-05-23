number = int(input("enter the number \n"))

reminder = number % 2

if reminder == 0:
    print(f"{number} is an even number")
else:
    print(f" {number} is an odd number")