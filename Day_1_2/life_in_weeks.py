print("calulcate the life in weeks")
age = int(input("enter your current age \n"))
maximum_age = 90
years_left = maximum_age - age
months_left = 12 * years_left
weeks_left = 4 * months_left
days_left = 365 * years_left
 
print(f"you have {days_left} days,{weeks_left} weeks,{months_left} months")