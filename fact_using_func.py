def factorial(n):
    fact=1
    if n==0 and n==1:
        return fact
    else:
        while n>1:
            fact=fact*n
            n=n-1
        return fact

a=int(input("enter a number"))
print (factorial(a))

