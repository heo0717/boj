import math

T = int(input().strip())

for i in range(1, T+1):
    L = list(map(int,input().split()))

    a, b, c = L

    if a + b <= c or a + c <= b or b + c <= a :
        print(f'Case #{i}: invalid!')
        continue

    if a == b == c :
        print(f'Case #{i}: equilateral')
        continue

    elif a == b or b == c or a == c :
        print(f'Case #{i}: isosceles')
        continue
        
    else :
        print(f'Case #{i}: scalene')