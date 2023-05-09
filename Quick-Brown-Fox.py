from collections import defaultdict

for _ in range(int(input())):
    alphabet_dict = defaultdict(lambda:0)
    for i in range(ord('a'),ord('z')+1):
        alphabet_dict[chr(i)]

    string = input().lower()
    for i in string:
        if i in alphabet_dict.keys():
            alphabet_dict[i]+=1
    missing_alphabet = ""
    for i in alphabet_dict.keys():
        if alphabet_dict[i] == 0:
            missing_alphabet+=i
    if len(missing_alphabet) == 0:
        print("pangram")
    else:
        print("missing "+missing_alphabet)