from collections import defaultdict

N = int(input())

while N > 0:
    
    item_list = []
    items_set = set()
    items_dict = defaultdict(lambda:[])
    for i in range(N):
        string_list = list(map(str, input().split()))
        for i in string_list[1:]:
            items_dict[i].append(string_list[0])
            if i not in items_set:
                item_list.append(i)
                items_set.add(i)
    item_list = sorted(item_list)
    for i in item_list:
        name_list = list(sorted(items_dict[i]))
        print(i,*name_list)
    
    N = int(input())