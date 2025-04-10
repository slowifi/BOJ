import sys

a = list(map(int, sys.stdin.readline().strip().split(' ')))

Days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Jan 1 1900: monday = 0
days = 0
days += a[2] - 1
months = a[1]
years = a[0]


for i in range(1, months):
    days += MonthDays[i-1]
if (a[0]%400 == 0) or (a[0]%4 == 0 and a[0]%100 != 0):
    if months > 2:
        days += 1

if years >= 1900:
    for i in range(1900, years):
        if (i%400 == 0) or (i%4 == 0 and i%100 != 0):
            days += 366
        else:
            days += 365
else:
    for i in range(years, 1900):
        if (i%400 == 0) or (i%4 == 0 and i%100 != 0):
            days -= 366
        else:
            days -= 365

# print(days)
# print(days%7)
print(Days[days%7])