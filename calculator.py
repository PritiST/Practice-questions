choice=input("""enter the operation required:
+ 
- 
* 
/ 
""")

a=float(input("enter first no"))
b=float(input("enter sec no"))

if choice=='+':
    
    print("Addition: " , a+b)
elif choice=='-':
    
    print("Subtraction: " , a-b)
elif choice=='*':
    
    print("Multiplication: " , a*b)
elif choice=='/':
    
    print("Division: " , a/b)
else:
    print("enter valid operation")





