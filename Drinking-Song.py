N = int(input())
beverage = input()

while N > 0:
    lesser=N-1
    if lesser == 1:
        print(f"{N} bottles of {beverage} on the wall, {N} bottles of {beverage}.\nTake one down, pass it around, {lesser} bottle of {beverage} on the wall.\n")
    elif N == 1:
        print(f"{N} bottle of {beverage} on the wall, {N} bottle of {beverage}.\nTake it down, pass it around, no more bottles of {beverage}.\n")
    else:
        print(f"{N} bottles of {beverage} on the wall, {N} bottles of {beverage}.\nTake one down, pass it around, {lesser} bottles of {beverage} on the wall.\n")
    N-=1
