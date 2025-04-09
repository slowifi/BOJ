import sys
from collections import deque


n, m = sys.stdin.readline().strip().split(' ')
n = int(n)
m = int(m)
Arr= [[] for _ in range(n)]
Visited = [[-1 for _ in range(m)] for _ in range(n)]
x,y = 0,0
nears = [[0,1],[1,0],[0,-1],[-1,0]]

for i in range(n):
    temp = sys.stdin.readline().strip().split(' ')
    if '2' in temp:
        y = i
        x = temp.index('2')
    Arr[i] = temp
    for j in range(len(temp)):
        if temp[j] == '0':
            Visited[i][j] = 0


q = deque()
q.append([x,y,0])
Visited[y][x] = 0

while q:
    a,b,v = q.popleft()
    # print(a,b,v)
    # print(q.qsize())
    for near in nears:
        c = a + near[0]
        d = b + near[1]
        if c < 0 or c >= m or d < 0 or d >= n:
            continue
        if Arr[d][c] == '0':
            Visited[d][c] = 0
            continue
        elif Visited[d][c] != -1:
            continue
        q.append([c,d,v+1])
        Visited[d][c] = v+1
    # break

for row in Visited:
    for ele in row:
        print(ele, end=' ')
    print()
