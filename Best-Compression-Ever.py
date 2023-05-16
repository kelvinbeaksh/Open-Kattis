N, b = map(int,input().split())

if len(str(bin(N))[2:]) <= b+1:
    print("yes")
else:
    print("no")