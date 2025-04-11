import sys

a = int(sys.stdin.readline().strip())
Arr = ['*', "**"]

if a== 0:
    print(Arr[0])
elif a == 1:
    print(Arr[1])
    print(Arr[0])

else:
    for i in range(1, a):
        for j in range(pow(2, i)):
            s = Arr[j]
            ss = s + " "*(pow(2,i) - j - 1) + s
            Arr.append(ss)

    for i in range(len(Arr)):
        print(Arr[-i-1])
