weather_c = eval(input())
# 🚨 Don't change code above 👆
#{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# Write your code 👇 below:
weather_f ={weather:(temp_c * 9/5) + 32 for weather,temp_c in weather_c.items()}


print(weather_f)