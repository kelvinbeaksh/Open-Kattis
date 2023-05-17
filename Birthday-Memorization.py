from collections import defaultdict

birthday_dates = defaultdict(lambda: None)

for _ in range(int(input())):
    Si, Ci, date = map(str, input().split(" "))
    if date not in birthday_dates.keys() or int(Ci) > birthday_dates[date][1]:
        birthday_dates[date] = (Si,int(Ci))
print(len(birthday_dates.keys()))
for i in sorted(list(birthday_dates.values())):
    print(i[0])