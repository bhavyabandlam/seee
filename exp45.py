s1="listen"
s2="silent"
count =0

for i in s1:
    if s1.count(i)==s2.count(i):
        count +=1
if count == len(s1):
    print("Anagram")
else:
    print("Not Anagram")
