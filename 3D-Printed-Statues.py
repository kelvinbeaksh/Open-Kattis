N = int(input())
minimum = 1
printer = 0
while N > (2**printer):
    printer+=1
    minimum+=1
print(minimum)