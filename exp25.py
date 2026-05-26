n=5
for i in range(n):
    ## spaces 
    for j in range(n-i-1):
        print(" ",end=" ")
    # Stars
    for j in range(i+1):
        print("*", end=" ")
    print()