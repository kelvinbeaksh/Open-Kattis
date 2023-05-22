from collections import defaultdict

pieces = defaultdict(lambda:0)

for _ in range(int(input())):
    sword_pieces = list(map(int,input()))
    for i in range(len(sword_pieces)):
        if sword_pieces[i] == 0:
            pieces[i]+=1

t_and_b = pieces[0]+pieces[1]
l_and_r = pieces[2]+pieces[3]
sword = min(t_and_b,l_and_r)//2

t_and_b-=(sword*2)
l_and_r-=(sword*2)

print(sword,t_and_b,l_and_r)