import sys

N = int(sys.stdin.readline().strip())

A = [0 for _ in range(N)]
IsDown = [0 for _ in range(N)]
for i in range(N):
    A[i] = int(sys.stdin.readline().strip())
    
    if i != 0:
        if A[i] > A[i-1]:
            IsDown[i-1] = 0
        else:
            IsDown[i-1] = 1

buy = False
USD = 100
MAR = 0
for i in range(N):
    if IsDown[i] == 1 and not buy:
        if 0 in IsDown[i:]:
            buy = True
            MAR = (A[i]/100) * USD
            USD = 0
    if IsDown[i] == 0 and buy:
        buy = False
        USD = (100/A[i]) * MAR
        MAR = 0
    # print(USD, MAR)

print("%.2f" %USD)