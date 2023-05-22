from collections import defaultdict
N,t = map(int,input().split())
A = list(map(int,input().split()))

if t == 1:
    print(7)
if t == 2:
    if A[0] < A[1]:
        print("Smaller")
    elif A[0] > A[1]:
        print("Bigger")
    else:
        print("Equal")
if t == 3:
    print(sorted(A[:3])[1])
if t == 4:
    print(sum(A))
if t == 5:
    print(sum(filter(lambda i:i%2==0,A)))
if t == 6:
    alphabet_dict = defaultdict(lambda:None)

    for i in range(26):
        alphabet_dict[i] = str(chr(i+97))
    string = ""
    for i in A:
        string+=str(alphabet_dict[i%26])
    print(string)

if t == 7:
    visited = {0}
    i = 0
    while True:
        i = A[i]
        
        if A[i] in visited:
            print("Cyclic")
            break
        elif A[i] == N-1:
            print("Done")
            break
        elif A[i] > N-1 or A[i] < 0:
            print("Out")
            break
        visited.add(i)
        

