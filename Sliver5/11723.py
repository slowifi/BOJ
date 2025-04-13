import sys

N = int(sys.stdin.readline().strip())

S = set()
for _ in range(N):
    inp = list(map(str, sys.stdin.readline().strip().split(' ')))
    if inp[0] == 'add':
        S.add(int(inp[1]))
    elif inp[0] == 'remove':
        if int(inp[1]) in S:
            S.discard(int(inp[1]))
    elif inp[0] == 'check':
        if int(inp[1]) in S:
            print(1)
        else:
            print(0)
    elif inp[0] == 'toggle':
        if int(inp[1]) in S:
            S.remove(int(inp[1]))
        else:
            S.add(int(inp[1]))
    elif inp[0] == 'all':
        S = set(i for i in range(1, 21))
    elif inp[0] == 'empty':
        S = set()
    
    # print(S)