string = input()
total = 0
for i in range(len(string)):
    total+=ord(string[i])
print(chr(total//len(string)))