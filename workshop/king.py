import sys
input = sys.stdin.readline

#setting ) col : A ~ H / row :  1 ~ 8
col = ['A','B','C','D','E','F','G','H']
row = ['1','2', '3', '4', '5', '6', '7', '8'] 

moves = {
    'L': (-1, 0),
    'R': (1, 0),  
    'T': (0, 1),   
    'B': (0, -1),  
    'LT': (-1, 1), 
    'LB': (-1, -1),
    'RT': (1, 1),
    'RB': (1, -1)  
}

k , r, n = input().strip().split()
N = int(n)

#1. seperate col , row

def seperate_char_num(A):
    char = ""
    num = ""

    for a in A :
        if a.isdigit(): num += a
        else: char += a
    
    return [char, num]

king = seperate_char_num(k)
rock = seperate_char_num(r)

#2. move king & rock

loc_k = [ col.index(king[0]), row.index(king[1]) ]
loc_r = [ col.index(rock[0]), row.index(rock[1]) ]

for _ in range(N):
    m = input().strip()

    dx, dy = moves[m]

    new_k_x = loc_k[0] + dx
    new_k_y = loc_k[1] + dy

    if not ( 0 <= new_k_x < 8 and 0 <= new_k_y < 8 ): continue

    if [new_k_x, new_k_y] == loc_r :
        new_r_x = loc_r[0] + dx
        new_r_y = loc_r[1] + dy

        if not ( 0 <= new_r_x < 8 and 0 <= new_r_y < 8 ): continue

        loc_r = [ new_r_x , new_r_y ]

    loc_k = [ new_k_x , new_k_y ]

print(col[loc_k[0]] + row[loc_k[1]])
print(col[loc_r[0]] + row[loc_r[1]])