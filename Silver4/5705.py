import sys

arr = [1, 2]

while 1:
    a = int(sys.stdin.readline().strip())
    if a == 0:
        break

    if a <= len(arr):
        print(arr[a-1])
    else:
        for i in range(len(arr), a):
            arr.append(arr[i-1] + arr[i-2])
        print(arr[a-1])

