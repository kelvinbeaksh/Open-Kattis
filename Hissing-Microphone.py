word = input()
result = "no hiss"
for i in range(len(word)-1):
    if word[i] == "s" and word[i+1] == "s":
        result="hiss"
        break       
print(result)  