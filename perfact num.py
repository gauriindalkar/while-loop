num=int(input("enter number"))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print("it is perfect number")
else:
    print("it is not perfect number")