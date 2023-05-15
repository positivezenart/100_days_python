bill =float(input("enter the final bill \n"))
number_of_people = int(input("enter the number of people \n"))

shared_amount = round(((bill / number_of_people) * 1.12),2) 
print("Each person should pay",'{:.2f}'.format(shared_amount))


