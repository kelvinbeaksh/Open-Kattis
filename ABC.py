abc_list = list(sorted(map(int, input().split())))
abc_dict = {"A":abc_list[0],"B":abc_list[1],"C":abc_list[2]}
x,y,z = [i for i in input()]
print(abc_dict[x],abc_dict[y],abc_dict[z])