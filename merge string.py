#list1 = ["ajay", "shankar", "tiwari"]


n = int(input("Enter the max size of array "))
list2 = []
for i in range(0,n):
    element = input("Enter the string to be inserted in list ")
    list2.append(element)
print(list2)


def merger(list1):
    a = ""
    for element in list1:
        a = a + element + " "
    return a


print(merger(list2))

list2.append("priti")
print(list2)
#print(merger(list1))

