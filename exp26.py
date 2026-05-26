n=5
for i in range(n):
    for s in range(n-i-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j, end=" ")
    print()