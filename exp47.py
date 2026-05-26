name="Programming"
duplicates=""

for i in name:
    if name.count(i)>1 and i not in duplicates:
        duplicates +=i
print(duplicates)
