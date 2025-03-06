import sys
input = sys.stdin.readline

n = int(input().strip()) #all_computer
m = int(input())

graph = [ [] for _ in range(n+1) ]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True #넣으면 일단 밟은것
    for i in graph[node]:
        if visited[i] == True : continue
        dfs(i)

dfs(1)

print(visited.count(True) - 1)