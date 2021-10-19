import sys

n, m = list(map(int, sys.stdin.readline().split()))
l = n-m
total = 1
if l > m:
    for i in range(n, m, -1):
        total *= i
    for i in range(l, 0, -1):
        total = total//i
else:
    for i in range(n, l, -1):
        total *= i
    for i in range(m, 0, -1):
        total = total//i
print(total)
