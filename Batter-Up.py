n = int(input())
bats = list(map(int, input().split()))
print(sum(list(filter(lambda i : i >=0,bats)))/len(list(filter(lambda i : i >=0,bats))))