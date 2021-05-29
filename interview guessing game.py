i=0
f=5
c=10
while c>0:
    u=int(input("enter number"))
    d=0
    if u==f:
        print("your guessing is correct")
        print("congrates")
        break
    elif u<f:
        d=f-u
        r=c-d
        if r>0:
            print("remaining chance",r)
        else:
            print("finished")
    elif f<u:
        d=u-f
        r=c-d
        if r>0:
            print("remaining chance",r)
        else:
            print("finished")
    i+=1
else:
    print("your chance is finished try again")