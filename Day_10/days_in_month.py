def is_leap(year):
  """Calculates leap year"""  
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  

def days_in_month(year, month):
  """ Number of days in a month"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  is_leap_year = is_leap(year)
  if is_leap_year:
      print("its a leap year")
      if month == 2:
        number_of_days =month_days[month-1] + 1
        return number_of_days
      else:
        number_of_days =month_days[month-1]
        return number_of_days
  else:
        print("Its not a leap year")
        number_of_days =month_days[month-1]
        return number_of_days

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

