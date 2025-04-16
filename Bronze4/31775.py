import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
s3 = sys.stdin.readline().strip()

ans = ["GLOBAL", "PONIX"]

if s1[0] == 'l' or s1[0] == 'k' or s1[0] == 'p':
    if s2[0] != s1[0] and (s2[0] == 'l' or s2[0] == 'k' or s2[0] == 'p'):
        if s3[0] != s1[0] and s3[0] != s2[0] and (s3[0] == 'l' or s3[0] == 'k' or s3[0] == 'p'):
            ans = ans[0]

if len(ans) == 2:
    ans = ans[1]

print(ans)
