vowels = {"A","E","I","O","U"}
count=0
for i in input().upper():
    if i in vowels:
        count+=1
print(count)
