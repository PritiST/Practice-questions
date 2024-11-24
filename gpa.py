mar_eng=float(input("enter english marks"))
mar_mat=float(input("enter maths marks"))
mar_sc=float(input("enter science marks"))
mar_ssc=float(input("enter social science marks"))
mar_hin=float(input("enter hindi marks"))
tot_mar=mar_eng+mar_mat+mar_sc+mar_ssc+mar_hin
av=tot_mar/500
per=av*100
print(tot_mar)
print(av)
print(per)
if(per>=80 and per==100):
    grade='A'
    print("your grade is A")
elif(per<=81 and per>70):
    grade='B'
    print("your grade is B")
elif(per<=71 and per>60):
    grade='C'
    print("your grade is C")
elif(per<=61 and per>40):
    grade='D'
    print("your grade is D")
elif(per<=41 and per>=30):
    grade='E'
    print("your grade is E")
else:
    grade='F'
    print("fail")

if(grade=='A'):
    gpa=4
    print("gpa is",gpa)
elif(grade=='B'):
    gpa=3
    print("gpa is",gpa)
elif(grade=='C'):
    gpa=2.5
    print("gpa is",gpa)
elif(grade=='D'):
    gpa=2
    print("gpa is",gpa)
elif(grade=='E'):
    gpa=1
    print("gpa is",gpa)
else:
    gpa=0
    print("gpa is",gpa)



