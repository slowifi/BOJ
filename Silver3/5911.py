import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))

Arr1 = []
Arr2 = []
ret = []

for _ in range(N):
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    Arr1.append(A)
    Arr2.append(B)
    

for i in range(N):
    data = []
    count = 0
    s = 0

    for j in range(N):
        if i == j:
            data.append(Arr1[j] // 2 + Arr2[j])
        else:
            data.append(Arr1[j] + Arr2[j])
    
    data.sort()
    #print(data)

    for j in range(N):
        s += data[j]
        if s > M:
            break
        count += 1
    ret.append(count)   
    #print(ret)
print(max(ret))


        