name=input("Enter a input: ")
new_name=""
for i in range(1,len(name)+1):
    if i%2==1:
        new_name +=name[i]
        new_name +=name[i-1]
print(new_name)