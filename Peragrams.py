from collections import defaultdict

string = input()
alphabet_map = defaultdict(lambda:0)
min_remove = 0

for i in string:
    alphabet_map[i]+=1

for i in alphabet_map.keys():
    if alphabet_map[i] % 2 != 0:
        min_remove+=(alphabet_map[i] % 2)

if min_remove > 0:
    min_remove-=1
    
print(min_remove)