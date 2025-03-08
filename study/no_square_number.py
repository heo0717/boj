import sys
input = sys.stdin.readline

min , max = map(int, input().split())

no_sqaure = [True] * (max - min + 1)  #True : no_sqaure

for i in range(2, int(max**0.5) + 1):
    square = i ** 2  
    #the first sqaure in range / using ceiling integer division (ceil(A/B))
    start = ((min + square - 1) // square) * square 

    for j in range(start, max + 1, square):
        no_sqaure[j - min] = False

print(sum(no_sqaure)) #bool => int / T = 1 , F = 0

#--------------------------------------------------time over

# square = []
# for i in range(2, int(max**0.5)+1): #max**0.5 == sqrt(max)
#     if i ** 2 <= max:
#         square.append(i**2)


# no_square = max - min + 1
# for i in range(min,max+1):
#     for j in square:
#         if i % j == 0:
#             no_square -= 1
#             break
                
# print(no_square)