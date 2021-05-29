i=1
num=5
while i<=num:
    guess=int(input("enter number"))
    i=i+1
    if num==guess:
        print("guessing is correct")
        print("congrates your winner")
        break
    else:
        print("guessing is incorrect")