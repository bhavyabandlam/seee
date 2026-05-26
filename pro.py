n=int(input("enter the number : "))

##create menu
choice=int(input("choose choice :"))
match choice:
    case 1:
        print("even /odd number")
    case 2:
        print("prime")
    case 3:
        print("palindrome")
    case 4:
        print("Armstrong")
    case 5:
        print("Reverse")
    case 6:
        print("Sum of digits")
    case _:
        print("not found")

if choice==1:
    if n%2==0:
        print("even")
    else:
        print("odd")
if choice==2:
    is_prime=True
    if n<=1:
        is_prime=False
    else:
        for i in range(2,n):
            if n %i==0:
                is_prime =False
                break
    if is_prime:
        print("prime Number")
    else:
        print("Not prime Number")
if choice==3:
    rev=0
    temp=n
    while temp>0:
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if n==rev:
        print("palindrome")
    else:
        print("not Panlindrome")
if choice==4:
    rev=0
    total=0
    temp=n
    while temp>0:
        r=temp%10
        total=total+(r**3)
        temp=temp//10
    if n==total:
        print("ARmstrong")
    else:
        print("Not Armstrong")
if choice==5:
    rev=0
    temp=n
    while temp>0:
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    print(rev)
if choice==6:
    total=0
    temp=n
    while temp>0:
        r=temp%10
        total+=r
        temp=temp//10
    print(total)


        