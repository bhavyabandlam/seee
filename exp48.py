name="programming"
duplicates=""

for i in range(len(name)):
    for j in range(i+1, len(name)):
        if name[i]==name[j] and name[i] not in duplicates:
            duplicates +=name[i]
print(duplicates)