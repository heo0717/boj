# BIG-O

a1, a0 = map(int, input().split()) #음수일수도 있음
c = int(input())
n = int(input()) # 1<=n0<=100

if a1 * n + a0 <= c * n and c >= a1:
    print(1)

else : print(0)