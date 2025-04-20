import sys
from collections import deque


n, m = map(int, sys.stdin.readline().strip().split(' '))
Arr= [[] for _ in range(n)]
Visited = [[-1 for _ in range(m)] for _ in range(n)]
x,y = 0,0
nears = [[0,1],[1,0],[0,-1],[-1,0]]

for i in range(n):
    Arr[i] = list(sys.stdin.readline().strip())
    for j in range(m):
        if Arr[i][j] == "I":
            y = i
            x = j
        if Arr[i][j] == 'X':
            Visited[i][j] = 0

# print(x, y)
# print(Arr)

q = deque()
q.append([x,y,0])
Visited[y][x] = 0

Met = 0
while q:
    a,b,v = q.popleft()
    # print(a,b,v)
    # print(q.qsize())
    for near in nears:
        c = a + near[0]
        d = b + near[1]
        if c < 0 or c >= m or d < 0 or d >= n:
            continue
        if Visited[d][c] != -1:
            continue
        if Arr[d][c] == 'P':
            Met += 1
        q.append([c,d,v+1])
        Visited[d][c] = v+1
    # break

# for row in Visited:
#     for ele in row:
#         print(ele, end=' ')
#     print()

if Met != 0:
    print(Met)
else:
    print("TT")