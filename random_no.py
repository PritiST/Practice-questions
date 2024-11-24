n=int(input("enter a random number between 1 and 100"))
if n<50 and n>=1:
    print("guess is too low", n)
elif n>=50 and n<=100:
    print("guess is too high", n)
else:
    print("enter no in given range")
