print('''      --------REMEMBER--------
      
    Underweight: BMI < 18.5
    Normal weight: 18.5 ≤ BMI < 24.9
    Overweight: 25 ≤ BMI < 29.9
    Obesity: BMI ≥ 30
      
      --------REMEMBER--------''')

weight = float(input("Please Enter Your Weight In KGs (Eg : 54.24) : "))
height = float(input("Please Enter Your Height In Meters (Eg : 1.75) : "))

height_squared = height * height
bmi = weight / height_squared
rounded_bmi = round(bmi, 2)

if rounded_bmi < 18.5:
    weight_type = "Underweight"
elif 18.5 <= rounded_bmi <= 24.9:
    weight_type = "Normal Weight"
elif 25 <= rounded_bmi <= 29.9:
    weight_type = "Overweight"
else:  
    weight_type = "Obese"

print("Your BMI is: " + str(rounded_bmi) + " and you are " + weight_type)
