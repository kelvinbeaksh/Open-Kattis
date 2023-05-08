N = int(input())
time_list = []
if N%2 == 1:
    print("still running")
else:
    for _ in range(N):
        time_list.append(int(input()))
    
    print(sum(time_list[1::2])-sum(time_list[0::2]))