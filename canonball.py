import sys

input = sys.stdin.readline
N, S = map(int, input().split())

q =[]
v = []
for i in range(N):
    Q, V= map(int,input().split())
    q.append(Q)
    v.append(V)

loc = S
p = 1
dir = 1
target = set()
visited = set()

if q[loc-1] == 0:
    p += v[loc-1]
    dir = -dir
elif q[loc-1] == 1 and p >= v[loc-1] and (loc-1) not in target :
    target.add(loc-1)

while True:

    movement = (loc, dir, p, frozenset(target))
    if movement in visited:
        break
    visited.add(movement)

    loc += dir * p

    if loc < 1 or loc > N :
        break

    if q[loc-1] == 0:
        p += v[loc-1]
        dir = -dir

    elif q[loc-1] == 1 and p >= v[loc-1] and (loc-1) not in target  :
        target.add(loc-1)

        
print(len(target)) 