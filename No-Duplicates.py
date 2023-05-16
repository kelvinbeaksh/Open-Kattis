line = list(map(str, input().split(" ")))

if len(set(line)) != len(line):
    print("no")
else:
    print("yes")