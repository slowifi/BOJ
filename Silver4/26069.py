import sys

N = int(sys.stdin.readline().strip())

ret = 1
Dance = ['ChongChong']
for _ in range(N):
    A, B = sys.stdin.readline().strip().split(' ')
    if A in Dance and B not in Dance:
        Dance.append(B)
    elif B in Dance and A not in Dance:
        Dance.append(A)
print(len(Dance))