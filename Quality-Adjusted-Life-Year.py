result = []
for _ in range(int(input())):
    q,y = map(float,input().split())
    result.append(q*y)
print(sum(result))