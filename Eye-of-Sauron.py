string = input()
result = "correct"
matching_dict = {"|":"|","(":")"}
if len(string)%2 == 1:
    result = "fix"
else:
    for i in range(int(len(string)//2)):
        if matching_dict[string[i]] != string[len(string)-i-1]:
            result="fix"
            break       
print(result)