#Creating a list
n = int(input("Enter the max size of array "))
list1 = []
for i in range(0,n):
    element = int(input("Enter the number to be inserted in list "))
    list1.append(element)
print(list1)

#Defining a function to find maximum element
def maximum(list1):
    max = 0
    for i in range(0,n):    
        if(max < list1[i]):
            max = list1[i]
    return max


#Passing the list to function
print("maximum element is", maximum(list1))

    