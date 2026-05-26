name="aaabbcc"
result=""
count =1

for i in range(len(name)-1):
    if name[i] == name[i+1]:
        count +=1
    else:
        result +=name[i] + str(count)
        count =1
result +=name[-1] +str(count)
print(result)