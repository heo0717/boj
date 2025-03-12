import sys
input = sys.stdin.readline

N, M = map(int, input().split())
#N = broken string num / M = guitar brand num

min_p = float('inf')
min_it = float('inf')


for i in range(M):
    p, it = map(int, input().split())
    min_p = min(min_p, p)
    min_it = min(min_it, it)

package = ( N // 6 ) * min_p
all_p = ((N//6)+1) * min_p
item = ( N % 6 ) * min_it
all_it = N * min_it

if all_p < package + item and all_p < all_it:
    print(all_p)

elif all_it < package + item and all_it < all_p :
    print(all_it)

else:
    print(package + item)

# -------------------------------------- compareing in one brand

# data = {}
# for i in range(M):
#     d = input().split()
#     data[i+1] = tuple(map(int, d))

#     #data[i][0] = package price / data[i][1] = item price

# case = []
# for i in range(1,M+1):
#     package = ( N // 6 ) * data[i][0]
#     all_package = ( ( N // 6 ) + 1 ) * data[i][0]
#     item = ( N % 6 ) * data[i][1]
    
#     if all_package > package + item :
#         case.append(package + item)
#     else :
#         case.append(all_package)

# print(min(case))