from collections import deque

def bfs(first):
    queue = deque([first])
    distances = {i: -1 for i in range(1, N + 1)} 
    distances[first] = 0

    while queue:
        now = queue.popleft()

        for friend in relationship[now]:
            if distances[friend] == -1:  
                distances[friend] = distances[now] + 1  
                queue.append(friend)

    return sum(distances.values()) 

N, M = map(int, input().split())
relationship = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    key, value = map(int, input().split())
    
    relationship[key].append(value)
    relationship[value].append(key)

min_bacon = float('inf')
answer = -1

for person in range(1, N + 1):
    bacon_score = bfs(person)  
    if bacon_score < min_bacon:  
        min_bacon = bacon_score
        answer = person

print(answer)