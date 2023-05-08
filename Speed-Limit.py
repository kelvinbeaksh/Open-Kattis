N = int(input())
while N != -1:
    distance_tracker = [(0,0)]
    total_distance = 0
    for i in range(N):
        s, t = map(int,input().split())
        distance_tracker.append((s,t))
    for i in range(1,len(distance_tracker)):
        total_distance+=(distance_tracker[i][0]*(distance_tracker[i][1]-distance_tracker[i-1][1]))
    print(f"{total_distance} miles")
    N = int(input())