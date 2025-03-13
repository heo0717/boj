n1 , n2 = map(int, input().split())

g1 = list(input())
g2 = list(input())

t = int(input())

ants = g1[::-1] + g2

for _ in range(t):
    j = 0
    while j < n1 + n2 -1 :
        if ants[j] in g1 and ants[j+1] in g2 :
            ants[j] , ants[j+1] = ants[j+1] , ants[j]
            j += 1
        j += 1

print(''.join(ants))