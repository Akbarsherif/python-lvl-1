


#1st

s=input("Enter the string: ")
n=int(s[0])
name=s[1:]
new_name=' '
for i in range(len(name)):
    if(i+1)%n==0:
        new_name+='z'
    else:
        new_name+=name[i]
print(new_name)


