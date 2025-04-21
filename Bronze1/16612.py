import sys

N, L = map(int, sys.stdin.readline().strip().split(' '))

for _ in range(N):
    temp = sys.stdin.readline().strip()
    L -= len(temp)

if N == 1:
    if L != 0:
        print("No")
    else:
        print("Yes")
elif L < 0:
    print('No')
elif L == 0 or L%(N-1) == 0:
    print('Yes')
else:
    print("No")