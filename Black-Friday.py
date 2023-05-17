from collections import defaultdict
N = int(input())
queue = list(map(int, input().split()))
roll_dict = defaultdict(lambda:0)
unique_roll = []
for i in queue:
    roll_dict[i]+=1

for i in roll_dict.keys():
    if roll_dict[i] == 1:
        unique_roll.append(i)
if len(unique_roll) > 0:
    print(queue.index(max(unique_roll))+1)
else:
    print("none")