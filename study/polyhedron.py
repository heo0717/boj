# Euler's Polyhedron Formula : V-E+F=2

T = int(input())

for _ in range(T):
    V, E = map(int, input().split())

    F = 2-V+E

    print(F)