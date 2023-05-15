l,h,v = map(int,input().split())

if h < l/2:
    h = l-h
if v < l/2:
    v = l-v

print(4*h*v)