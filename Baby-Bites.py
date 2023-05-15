N = int(input())
counting_list = list(map(str,input().split(" ")))
result = "makes sense"

for i in range(1,N+1):
    if counting_list[i-1] != str(i) and counting_list[i-1] != "mumble":
        result = "something is fishy"
        break
print(result)