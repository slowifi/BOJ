import sys

a1 = list(map(float, sys.stdin.readline().strip().split(' ')))
a2 = list(map(float, sys.stdin.readline().strip().split(' ')))

r = []
for i in range(5):
    r.append(round(2 * a1[4-i] - a2[4-i] , 3))
# r = r.reverse()

if r[2] <= 0:
    r[3] -= 1
    r[2] += 30
elif r[2] > 30:
    r[3] += 1
    r[2] -= 30
if r[3] <= 0:
    r[4] -= 1
    r[3] += 12
elif r[3] > 12:
    r[4] += 1
    r[3] -= 12
print(int(r[4]), int(r[3]), int(r[2]), end=" ")
for i in range(2):
    print("%.3f" % r[1-i], end=" ")

