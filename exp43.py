name="education"
vowels="aeiou"
for i in name:
    if i in vowels:
        print("*", end="")
    else:
        print(i,end="")