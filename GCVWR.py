G,T,N = map(int,input().split())
items_weight = sum(map(int,input().split()))
print(int(((G-T)*0.9)-items_weight))