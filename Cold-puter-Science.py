n = int(input())
count = 0
for i in map(int,input().split()):
    if i<0:
        count+=1
print(count)