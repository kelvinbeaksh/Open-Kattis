N = int(input())
word_list = []
check_list = []

for i in range(N):
    word_list.append(input())
    if len(word_list) > 1:
        if word_list[i] > word_list[i-1]:
            check_list.append(1)
        elif word_list[i] < word_list[i-1]:
            check_list.append(-1)

if len(set(check_list)) > 1:
    print("NEITHER")
elif list(set(check_list))[0] == 1:
    print("INCREASING")
else:
    print("DECREASING")