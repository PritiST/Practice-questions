def si(p,r,t):
   interest=(p*(r/4)*t)/100
   return interest

pr=float(input("enter principle amount: "))
ra=float(input("enter rate of interest quaterly: "))
ti=float(input("enter time: "))
simple_interest=si(pr,ra,ti)
print(simple_interest)