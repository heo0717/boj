n = int(input())

# comb = []
# sum = 0
# for i in range(1, n-1):
#     for j in range(i+1, n):
#         for k in range(j+1, n+1):
#             # i < j < k 

#             comb.append([i,j,k])
#             sum += i * j * k

# print(sum)
# print(comb)

#---------------------------------------
# cnt = 0
# for i in range(n-1):
#     if i == 1: cnt += 1
#     else:
#         cnt += i * (i+1) // 2
#print(cnt)
#---------------------------------------

print(n*(n-1)*(n-2)//6)
print(3)