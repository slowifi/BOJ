import sys
import math

mod = 1000000007

def fact(N):
    x = 1
    for i in range(1, N + 1):
        x = (x * i)%mod
    return x

N, K = map(int, sys.stdin.readline().strip().split(' '))

def pow(base, s):
    if s == 0:
        return 1
    elif s == 1:
        return base
    else:
        temp = pow(base, s//2) % mod
        if s%2 == 1:
            return ( temp%mod * temp%mod * base%mod)%mod
        else:
            return ( temp * temp)%mod


# Comb = math.comb(N,K)
# print(Comb)
fn = fact(N)
fk = (fact(K) * fact(N-K)) % mod
M = (fn * pow(fk, mod-2)) % mod

print(M)
