from collections import defaultdict
from heapq import heappush, heappop

count_dict = defaultdict(lambda:0)
N,K = map(int,input().split())
line = list(map(int,input().split()))
for i in line:
    count_dict[i]+=1

count_list = [i for i in count_dict.values()]

if K == 0:
    print(max(count_list))
else:
    count_list = sorted([-i for i in count_list])
    while K > 0:
        num = heappop(count_list)
        heappush(count_list,num+1)
        K-=1
    print(max([-i for i in count_list])) 
    
