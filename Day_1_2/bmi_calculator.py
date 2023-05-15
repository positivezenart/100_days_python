#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
def bmi_calculator(weight,height):
    bmi = weight / (height**2)
    return bmi

weight = int(input("enter your weight in kG: \n"))
height =float(input("Enter your height in meters: \n"))
bmi = weight / (height**2)
print(f"Your BMI is, {bmi_calculator(weight,height)}")