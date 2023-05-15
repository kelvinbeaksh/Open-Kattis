for _ in range(int(input())):
    D_list = list(map(str,input().split(",")))
    number = 0
    for i in range(len(D_list)):
        if D_list[i] != "":
            number+=(int(D_list[i])*(60**(len(D_list)-i-1)))
    print(number)