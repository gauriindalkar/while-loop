n=int(input("enter number"))
i=1
s=0
while i<n:
    if n%1==0:
        print(i)
        s=s+1
    i=i+1
if s==2:
    print(n,"is prime number")
else:
    print(n,"is not prime number")