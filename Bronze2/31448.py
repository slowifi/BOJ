import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split(' ')))

retList = [0]

for i in range(1, N):
    if A[i-1] < A[i]:
        retList.append(retList[i-1]+A[i]-A[i-1])
    else:
        retList.append(0)
print(max(retList))