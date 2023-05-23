year = int(input("Enter the year \n"))

if year %4 ==0:
    if year %100 == 0 and year %400 ==0:
        print(f"{year} is Leap year")
    elif year %100 !=0:
        print(f"{year} is Leap year")
    elif year %100 == 0 and year %400 !=0:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is Not a leap year")         
