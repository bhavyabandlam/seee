sum=0
n=12344
while n>0:
    r=n% 10
    sum+=r
    n=n//10
print(sum)