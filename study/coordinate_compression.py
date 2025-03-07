import sys
input = sys.stdin.readline

N = int(input()) #len(x_coords)
x_coords = list(map(int, input().split()))

sorted_x = sorted(set(x_coords))
dict_x = { value:index for index, value in enumerate(sorted_x)}

compressed_coords = []
for x in x_coords :
    compressed_coords.append(dict_x[x])  

print(*compressed_coords)