chess_pieces_list = [1,1,2,2,2,8]
input_pieces = list(map(int,input().split()))

for i in range(len(input_pieces)):
    chess_pieces_list[i]-=input_pieces[i]

print(*chess_pieces_list)