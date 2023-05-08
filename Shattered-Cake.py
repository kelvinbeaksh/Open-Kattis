#Solution A
w = int(input())
area = 0
for _ in range(int(input())):
    wi,li = map(int,input().split())
    area+=(wi*li)

print(int(area/w))

#Solution B (slowest)
w = int(input())
area_list = []
for _ in range(int(input())):
    wi,li = map(int,input().split())
    area_list.append(wi*li)

print(int(sum(area_list)/w))

#Solution C
from collections import defaultdict
w = int(input())
cake_pieces = defaultdict(lambda:0)
for _ in range(int(input())):
    wi,li = map(int,input().split())
    cake_pieces[wi*li] +=(wi*li)

print(int(sum(cake_pieces.values())/w))