n=int(input("enter number"))
i=1
while i<=n:
    b=1
    while b<=n-i:
        print(end=" ")
        b=b+1
    a=1
    while a<=i:
        print("*",end=" ")  
        # print(i,end="")
        a=a+1
    print()
    i=i+1