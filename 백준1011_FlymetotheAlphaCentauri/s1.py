import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    x, y = list(map(int, input().split()))
    z = y - x
    i = 1
    while i**2 > z or z >= (i+1)**2:
        i += 1
    total = i**2
    cnt = 2*i-1
    remain = z-total
    while remain-i >= 0:
        remain -= i
        cnt += 1
    if remain != 0:
        total += 1
        cnt += 1

    print(cnt)
