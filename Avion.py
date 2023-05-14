name_list = []
for i in range(1,6):
    name = input()
    if "FBI" in name:
        name_list.append(i)

if len(name_list) > 0:
    print(*name_list)
else:
    print("HE GOT AWAY!")