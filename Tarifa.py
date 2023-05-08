X = int(input())
N = int(input())
total_usage = 0
for _ in range(N):
    total_usage+=int(input())
print((X*(N+1))-total_usage)