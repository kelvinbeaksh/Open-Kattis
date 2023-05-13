N = int(input())
while N > 0:
    vowels_count_list = []
    for i in range(N):
        vowels_count_dict = {"aa":0,"ee":0,"ii":0,"oo":0,"uu":0, "yy":0}
        word = input().lower()
        for i in range(len(word)-1):
            if (word[i] + word[i+1]) in vowels_count_dict.keys():
                vowels_count_dict[word[i] + word[i+1]] += 1
        vowels_count_list.append((sum(vowels_count_dict.values()),word))        
    print(sorted(vowels_count_list)[-1][1])
    N = int(input())