n=153
temp=n
total = 0
while temp >0:
    r=temp %10
    total=total +(r**3)
    temp = temp // 10
if n == total:
    print("Armstrong Number")
else:
    print("Not Armstrong")