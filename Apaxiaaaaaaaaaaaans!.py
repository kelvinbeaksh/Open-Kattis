string = input()
filteredString = "0"

for i in string:
    if i != filteredString[-1]:
        filteredString+=i
print(filteredString[1:])