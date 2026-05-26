name="education"
vowels="aeiou"

result=""
for i in name:
    if i in vowels:
        result +="*"
    else:
        result +=i
print(result)