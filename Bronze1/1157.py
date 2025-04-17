import sys

s = sys.stdin.readline().strip().upper()
ss = list(set(s))
# print(ss)
sss = [0 for _ in range(len(ss))]
temp = 0
m = -1
mm = 0
for l in ss:
    c = s.count(l)
    if c > m:
        m = c
        mm = 0
    elif c == m:
        mm += 1
    sss[temp] = c
    temp += 1
# print(sss)
if mm != 0:
    print("?")
else:
    print(ss[sss.index(max(sss))])