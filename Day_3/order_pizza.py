print("Welome to python pizza delivery service")
size = input('Enter the size of the pizza(s,m,l) you wish to \n')
add_peporoni = input("do you want to add peporoni? (yes/no)")
Extra_cheese = input("do you want to add extra cheese?(yes/no)")
bill =0
if size =='s':
    bill += 15
    if add_peporoni == 'yes':
        bill +=2
elif size =='m':
    bill += 20
else:
    bill += 25
if add_peporoni == 'yes':
    if size == 's':
       bill += 2
    else:
       bill += 3
else:
    bill += 0
if Extra_cheese == 'yes':
    bill +=1
else:
    bill += 0
    
print(f"your final bill is ${bill}")

