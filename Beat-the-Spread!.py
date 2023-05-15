for _ in range(int(input())):
    s,d = map(int, input().split())
    s1 = int(((s-d)/2))+d
    s2 = int((s-d)/2)
    if s < d or s1+s2 != s:
        print("impossible")
    else:
        print(s1,s2)