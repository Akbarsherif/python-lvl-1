#4th

def is_armstrong(num):
    n=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**n
        temp//=10
    return num ==sum
list=list(map(int,input("Enter the list of number: ").split()))
for i in range(len(list)):
    if is_armstrong(list[i]):
        list[i]=1
    else:
        list[i]=0
print(list)
