n=int(input("enter a specified no: "))
f_no=0
sec_no=1
nxt_no=f_no+sec_no
i = 0
if i==1:
    print(f_no)
elif i==2:
    print(f_no)
    print(sec_no)
else:
    while (i<n):
        print(f_no)
        f_no=sec_no
        sec_no=nxt_no
        nxt_no=f_no+sec_no
        i=i+1


    
    