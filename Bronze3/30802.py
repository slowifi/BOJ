import sys

n = int(sys.stdin.readline().strip())
Size = list(map(int, sys.stdin.readline().strip().split(' ')))
T, P = map(int, sys.stdin.readline().strip().split(' '))

shirt = 0
for s in Size:
    if s%T == 0:
        shirt += s//T
    else:
        shirt += s//T + 1
print(shirt)

print(n//P, n%P)