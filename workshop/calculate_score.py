import sys
input = sys.stdin.readline

S = [ int(input().strip()) for _ in range(8) ]

SC = [ (idx , value) for idx, value in enumerate(S) ]

sorted_SC = sorted(SC, key= lambda x: x[1], reverse = True)

score = 0
q = []
for i in range(5):
    q.append(sorted_SC[i][0] + 1)
    score += sorted_SC[i][1]

question = sorted(q)

print(score)
print(*question)