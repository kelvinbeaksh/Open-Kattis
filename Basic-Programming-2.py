from collections import defaultdict

N,t = map(int,input().split())
A=list(map(int,input().split()))

if t == 1:
    A = sorted(A)
    result = "No"
    start,end = 0,N-1
    while start != end:
        if A[start]+A[end]==7777:
            result = "Yes"
            break
        elif A[start]+A[end]>7777:
            end-=1
        else:
            start+=1
        
    print(result)
    
if t == 2:
    if len(set(A)) == len(A):
        print("Unique")
    else:
        print("Contains duplicate")
    
if t == 3:
    count_dict = defaultdict(lambda:0)
    result = -1
    for i in A:
        count_dict[i]+=1
    for i in count_dict.keys():
        if count_dict[i] > (N/2):
            result = i
    print(result)
    
if t == 4:
    A = sorted(A)
    if N%2 == 1:
        print(A[int((N//2))])
    else:
        print(A[int(N/2)-1],A[int((N/2))])
    
if t == 5:
    A = filter(lambda i: i>=100 and i<=999,sorted(A))
    print(*A)