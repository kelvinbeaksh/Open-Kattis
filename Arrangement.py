N = int(input())
M = int(input())

groupings = []
remainder = M%N

for _ in range(N):
    if remainder != 0:
        groupings.append(int(M//N)+1)
        remainder-=1
    else:
        groupings.append(int(M//N))

for i in groupings:
    print(i*'*')