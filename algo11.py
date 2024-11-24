from tabulate import tabulate

Departments = [
    ["CSE",25],
    ["civil",23],
    ["electrical",34],
    ["electronic",45],
    ["mechanical",34]
]

headers=["Department","No of students"]
print(tabulate(Departments, headers, tablefmt="grid"))


Students_Info =[
    ["abc",23],
    ["sdf",32],
    ["fgh",24]
]
headers1=["Name of Students","Age"]
print(tabulate(Students_Info, headers1, tablefmt="grid"))


Employee=[
    ["Ajay",20000.00],
    ["Anay",3400.56],
    ["Aman",3498.56]
]
headers2=["Empl_name","sal"]
print(tabulate(Employee,headers2,tablefmt="grid"))