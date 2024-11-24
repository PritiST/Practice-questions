n=int(input("Enter any number"))
order=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp = temp//10

if n==sum:
    print(n,"is an armstrong no")
else:
    print(n,"is not an armstrong no")
