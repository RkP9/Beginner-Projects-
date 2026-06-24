# BMI Calculator 

def convert_units(weight_lbs, height_inch):
  weight_kg = float(weight / 2.25)
  height_m = float(height * 0.025)
  return weight_kg , height_m


def bmi_calc(weight, height):
  bmi = weight / (height ** 2)
  if bmi <18.5:
    print(f"BMI is {bmi} : Subject Underweight")
  elif 18.5 <= bmi <24.9:
    print(f"BMI is {bmi} : Healthy Weight")
  elif 25 < bmi < 29.9:
    print(f"BMI is {bmi} : Overweight")
  elif 30 <= bmi < 34.9:
    print(f"BMI is {bmi} : Obese")
  elif 35 <= bmi:
    print(f"BMI is {bmi} : Severely Obese")
  else: 
    print("Invalid Input")


print("Press 1 for metric units")
print("Press 2 for imperial units")

input_units = int(input("Choose 1 or 2: "))

if input_units == 1:
    print("Metric Units")
elif input_units == 2:
    print("Imperical Units")
else: 
    print("Invalid Input")

input_weight  = input("Enter your weight: ")
input_height  = input("Enter your height: ") 

weight = float(input_weight)
height = float(input_height)


if input_units == 2:
  weight, height = convert_units(weight, height)


bmi_calc(weight, height)
