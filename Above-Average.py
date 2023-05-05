for _ in range(int(input())):
    numbers = list(map(int,input().split()))
    count=0
    for i in numbers[1:]:
        if i > sum(numbers[1:])/numbers[0]:
            count+=1
    print("{:.3f}%".format((count/numbers[0])*100))