A_u,B_u,A_r,B_r = map(int,input().split())

result = A_r * B_r

if A_r > 0:
    result+=B_u
if B_r > 0:
    result+=A_u

if A_r == 0 and B_r == 0:
    result+=min(A_u,B_u)

print(result)