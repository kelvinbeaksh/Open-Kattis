A,B = 0,0
line = input()
for i in range(0,len(line),2):
    if line[i] == "A":
        A+=int(line[i+1])
    if line[i] == "B":
        B+=int(line[i+1])

if A > B:
    print("A")
else:
    print("B")