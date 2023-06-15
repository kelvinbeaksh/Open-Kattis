A,B  = map(str,input().split(" "))
position_a, position_b = 0,0
same = False
  
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            position_a, position_b = j,i
            same = True
            break
    if same:
        break

for i in range(len(B)):
    line = ""
    for j in range(len(A)):
        if j == position_b:
            line+=B[i]
        elif i == position_a:
            line+=A[j]
        else:
            line+="."
    print(line)
