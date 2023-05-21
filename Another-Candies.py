for _ in range(int(input())):
    blank = input()
    total = 0
    N = int(input())
    for i in range(N):
        total+=int(input())
    if total%N == 0:
        print("YES")
    else:
        print("NO")