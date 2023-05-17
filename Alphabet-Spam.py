string = input()

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0

for i in string:
    if ord(i) in range(97,123):
        lowercase+=1
    elif ord(i) in range(65,91):
        uppercase+=1
    elif i == "_":
        whitespace+=1
    else:
        symbols+=1

print(whitespace/len(string))
print(lowercase/len(string))
print(uppercase/len(string))
print(symbols/len(string))


