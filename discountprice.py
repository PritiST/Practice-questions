amt=int(input("enter purchase amount in dollars"))
if amt>=100:
    disc=amt*0.1
    final_price=amt-disc
    print("price after discount is",final_price)
else:
    print("no discount on purcahse amount")