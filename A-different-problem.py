import sys
for line in sys.stdin.readlines():
    a1,a2 = map(int,line.split())
    print(abs(a1-a2))
