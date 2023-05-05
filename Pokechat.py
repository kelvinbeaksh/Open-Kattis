from collections import defaultdict

S_dict = defaultdict(lambda:None)
result = ""
for i,e in enumerate(input()):
    S_dict[i+1] = e
    
number = int(input())
number_list = []

while number>0:
    number_list.append(number%1000)
    number//=1000

for i in number_list[::-1]:
    result+=S_dict[i] 
    
print(result)