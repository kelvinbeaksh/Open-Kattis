line = list(map(int,input().split()))

for i in range(len(line)-1):
    for i in range(len(line)-1):
        if line[i] > line[i+1]:
            line[i],line[i+1] = line[i+1], line[i]
            print(*line)