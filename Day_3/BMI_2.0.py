def bmi_calculator(weight,height):
    bmi = weight / (height**2)
    return round(bmi,2)

weight = int(input("enter your weight in kG: \n"))
height =float(input("Enter your height in meters: \n"))
bmi_index = bmi_calculator(weight,height)

if bmi_index <= 18.5:
    print(f"your BMI is {bmi_index},you are underweight")
elif bmi_index >= 18.5 and bmi_index <= 25:
    print(f"your BMI is {bmi_index},you have a normal weight")
elif bmi_index >= 25 and bmi_index <= 30:
    print(f"your BMI is {bmi_index},you are slightly overweight")
elif bmi_index >= 30 and bmi_index <= 35:
    print(f"your BMI is {bmi_index},you are obese")
elif bmi_index >= 35:
    print(f"your BMI is {bmi_index},you are clinically obese")