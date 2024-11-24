yr=int(input("enter a year"))
if ((yr % 4 == 0) and (yr % 400 == 0 or yr % 100!=0)):
    print("leap year")
else:
    print("not leap year")