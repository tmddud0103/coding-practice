import sys
from math import lcm
sys.stdin = open('input.txt')

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    m, n, x, y = list(map(int, sys.stdin.readline().split()))
    lmn = lcm(m, n)
    a = 0
    k = x - y
    while m*a < lmn:
        if k%n==0:
            print(m*a+x)
            break
        k += m
        a+=1
    if m*a >= lmn:
        print(-1)