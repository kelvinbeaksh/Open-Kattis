book_list = []
for _ in range(int(input())):
    book_list.append(int(input()))
sorted_book_prices = list(reversed(sorted(book_list)))
total=0
start,end=0,3
while start < len(book_list):
    total+=sum(sorted_book_prices[start:end-1])
    start+=3
    end+=3
print(total)   
    