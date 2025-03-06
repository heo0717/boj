import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokedex = {}
name_to_index = {}

for i in range(1, N+1):
    name = input().strip()
    pokedex[i] = name
    name_to_index[name] = i

for _ in range(M):
    q = input().strip()

    if q.isdigit():
        print(pokedex[int(q)])
    else:
        print(name_to_index[q])