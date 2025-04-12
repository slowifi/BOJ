import sys

n = int(sys.stdin.readline().strip())

for j in range(n):
    data = list(map(str, sys.stdin.readline().strip().split(' ')))

    Time_O = 0
    Time_B = 0
    Time = 0
    Pos_O = 1
    Pos_B = 1
    for i in range(int(data[0])):
        if data[i*2 + 1] == "O":
            Time_O = max(Time_O + abs(int(data[i*2 + 2]) - Pos_O), Time_B) + 1
            Pos_O = int(data[i*2 + 2])
        else:
            Time_B = max(Time_B + abs(int(data[i*2 + 2]) - Pos_B), Time_O) + 1
            Pos_B = int(data[i*2 + 2])
        # print(Time_B, Time_O)
    print("Case #%d: " %(j+1), end="")
    print(max(Time_O, Time_B))