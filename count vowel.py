txt=(input("enter any string including vowels"))
v='AEIOUaeiou'
count=0
for letter in txt:
    if letter in v:
        count=count+1
print(count)