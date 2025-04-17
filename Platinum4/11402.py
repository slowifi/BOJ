import sys
import math

N, K, mod = map(int, sys.stdin.readline().strip().split(' '))

def base(x, m):
    coeffs = []
    while x > 0:
        temp = x%m
        coeffs.append(temp)
        x = (x - temp)//m
        # print(temp, x)
    return coeffs

c1 = base(N, mod)
c2 = base(K, mod)
# print(c1)
# print(c2)
if len(c1) > len(c2):
    for _ in range(len(c2), len(c1) + 1):
        c2.append(0)
elif len(c2) > len(c1):
    for _ in range(len(c1), len(c2) + 1):
        c1.append(0)

# c1.reverse()
# c2.reverse()

ret = 1
for i in range(len(c1)):
    if c2[i] > c1[i]:
        ret = 0
        break

    elif c2[i] == 0 or c1[i] == c2[i]:
        continue
    elif c2[i] == 1 or c1[i]-c2[i] == 1:
        ret = ret * c1[i] % mod

    else:
        ret *= math.comb(c1[i], c2[i])%mod
    

print(ret%mod)
