r,n = map(int,input().split())
room_list = [i for i in range(1,r+1)]

for _ in range(n):
    booked = int(input())
    room_list[booked-1] = "booked"
    
result = "too late"

for i in range(r):
    if room_list[i] != "booked":
        result=room_list[i]
        break

print(result)