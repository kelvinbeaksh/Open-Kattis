scores = []
for i in range(1,6):
    scores.append((sum(map(int, input().split())),i))
scores = sorted(scores)
print(scores[-1][1],scores[-1][0])