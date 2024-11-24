n=int(input("enter a no to find factorial"))
fact=1
if n==0 and n==1:
    print("factorial of 0 and 1 is",fact)
else:
    while n>1:
        fact=fact*n
        n=n-1
    print("factorial of no greater than 1 is",fact)
    