l,r = map(int,input().split())
if l != r:
    print(f"Odd {max(l,r)*2}")
elif l == 0 and r == 0:
    print("Not a moose")
else:
    print(f"Even {l+r}")