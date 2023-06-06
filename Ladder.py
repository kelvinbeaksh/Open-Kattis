import math

h,v = map(int,input().split())
if h%math.sin(math.radians(v)) != 0:
    print(int(h//math.sin(math.radians(v)))+1)
else:
    print(int(h//math.sin(math.radians(v))))