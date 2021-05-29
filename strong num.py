num=int(input("enter number"))
a=num
sum1=0
while num:
    i=1
    f=1
    r=num%10
    while i<=r:
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if sum1==a:
    print("this is strong number")
else:
    print("this is not strong number")

