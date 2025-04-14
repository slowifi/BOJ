import sys
sys.setrecursionlimit(2000)


def dfs(i, visited):
    visited[i] = 1
    for v in graph[i]:
        if visited[v-1] == 0:
            dfs(v-1, visited)
        # visited[v] = 1
    return True


a, b = map(int, sys.stdin.readline().strip().split(' '))
graph = [[] for _ in range(a)]
visited = [0 for _ in range(a+1)]
result = 0

for i in range(b):
    c, d = map(int, sys.stdin.readline().strip().split(' '))
    graph[c-1].append(d)
    graph[d-1].append(c)
#print(graph)

for i in range(a):
    if visited[i] != 1:
        dfs(i, visited)
        result += 1

print(result)
