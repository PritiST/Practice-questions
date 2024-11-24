a=float(input("enter assignment marks"))
m=float(input("enter midterm marks"))
f=float(input("enter final marks"))
f_g=((a*0.4)+(m*0.3)+(f*0.3))
if f_g>=90:
    print("Grade A")
elif f_g>=70:
    print("Grade B")
elif f_g>=50:
    print("Grade C")
elif f_g>=30:
    print("Grade C")