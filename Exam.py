N = int(input())
friend = input()
you = input()

same, different = 0,0

for i in range(len(friend)):
    if friend[i] == you[i]:
        same+=1
    else:
        different+=1
if same >= N:
    print(N+different)
else:
    N-=same
    different-=N
    print(same+different)
