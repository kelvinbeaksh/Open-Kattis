while True:
    vectors=sorted(list(map(int,input().split())))
    
    if vectors[0] == 0 and vectors[1] == 0 and vectors[2] == 0:
        break
    if (vectors[0]**2)+(vectors[1]**2)==(vectors[2]**2):
        print("right")
    else:
        print("wrong")
