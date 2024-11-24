def prime(n):
        if n<=1:
             return False
        for i in range(2,int((n/2)+1)):
            if n%i==0:
                return -1
        return True
        
            
x=int(input("enter a number "))
if (prime(x) == -1):
    print("Not a prime number")
else:
    print("Prime number")      