wt=float(input("enter your weight in kg"))
ht=float(input("enter your height in meter"))
BMI=(wt/(ht*ht))
if BMI<18.5:
    print("Underweight")
elif 18.5<=BMI<24.9:
    print("Normal weight")
elif 25.0<=BMI<29.9:
    print("Overweight")
elif BMI>=30:
    print("Obesity")
else:
    print("enter proper measurement")
