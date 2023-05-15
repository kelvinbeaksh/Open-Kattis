from collections import defaultdict

dictionary = defaultdict(lambda:None)

while True:
    line = input()
    if line == "":
        break
    else:
        k,v = map(str,line.split(" "))
        dictionary[v] = k

while True:
    try:
        word = input()
        if word in dictionary.keys():
            print(dictionary[word])
        else:
            print("eh")
    except EOFError:
        break

