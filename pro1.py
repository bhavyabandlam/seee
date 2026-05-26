##String Analyzer
name =input("Enter a String: ")
##1 Total characters
print("Total characters:",len(name))
##2 Total words
words=name.split()
print("Total words:",len(words))

##3 vowel count
vowels = "aeiouAEIOU"

vowel_count=0

for i in name:
    if i in vowels:
        vowel_count +=1
print("Vowels:",vowel_count)
##4 uppercase count
upper = 0
for i in name:
    if i.isupper():
        upper +=1
print("Uppercase:",upper)

## 5 Lowercase count
lower =0
for i in name:
    if i.islower():
        lower +=1
print("Lower case:",lower)

## 6 Reverse String
reverse=""
for i in name:
    reverse=i+ reverse
print("Reverse:",reverse)

## 7 palindrome checkk
temp= name.replace(" ","").lower()
if temp==temp[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

##8 Remove spaces
print("without spaces:",name.replace(" ",""))

##9 largest word
largest=""

for i in words:
    if len(i) > len(largest):
        largest =i
print("Largest word:", largest)

##10 Duplicate characters
duplicates=""
for i in name.lower():
    if i !=" " and name.lower().count(i)>1 and i not in duplicates:
        duplicates +=i
print("Duplicates: ",duplicates)