name="I love programming language"
word=""
largest=""
for i in name:
    if i !=" ":
        word +=i
    else:
        if len(word)> len(largest):
            largest=word
        word = ''
if len(word) > len(largest):
    largest=word
print(largest)