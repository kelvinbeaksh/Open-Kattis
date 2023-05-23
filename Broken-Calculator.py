result = 1
for _ in range(int(input())):
    n1,operator,n2 = map(str,input().split(" "))
    if operator == "*":
        result = (int(n1)*int(n2))**2
    if operator == "+":
        result = (int(n1)+int(n2))-result
    if operator == "-":
        result*=(int(n1)-int(n2))
    if operator == "/":
        if int(n1)%2 == 0:
            result = int(int(n1)/2)
        else:
            result = int((int(n1)+1)/2)
    
    print(result)