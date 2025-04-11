import sys
from collections import deque


n = int(sys.stdin.readline().strip())

q = deque()

for _ in range(n):
    temp = sys.stdin.readline().strip()
    order = ""
    val = ""
    if " " in temp:
        order, val = temp.split(" ")
        val = int(val)
    else:
        order = temp

    if order == "push":
        q.append(val)
    elif order == "pop":
        if (len(q)) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif order == "front":
        if (len(q)) == 0:
            print(-1)
        else:
            f = q.popleft()
            print(f)
            q.appendleft(f)
    elif order == "back":
        if len(q) == 0:
            print(-1)
        else:
            b = q.pop()
            print(b)
            q.append(b)
    elif order == "size":
        print(len(q))
    elif order == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

