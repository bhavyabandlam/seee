name ="I love programming language"
words=name.split()

largest=""
for i in words:
    if len(i)> len(largest):
        largest =i
print(largest)
