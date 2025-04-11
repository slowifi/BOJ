import sys

N, B = map(int, sys.stdin.readline().strip().split(' '))

P = []
S = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    P.append(A)
    S.append(B)