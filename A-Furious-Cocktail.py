N,T = map(int,input().split())
potion_list=[]
for i in range(N):
    potion_list.append(int(input()))
reversed_list = list(reversed(sorted(potion_list)))
result="YES"
for i in range(N):
    if reversed_list[i] <= (T*(N-i-1)):
        result="NO"
        break
print(result)