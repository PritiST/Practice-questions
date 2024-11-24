age=float(input("enter your age"))
status=input("enter 'Y' for YES and 'N' for NO").upper()
if age<18 and status=='N':
    print(" not registered and ineligible to vote")
else:
    print(" Registered and eligible to vote")