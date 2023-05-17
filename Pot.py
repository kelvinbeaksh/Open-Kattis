result = 0
for _ in range(int(input())):
    P = int(input())
    result+=((P//10)**(P%10))
print(result)
    