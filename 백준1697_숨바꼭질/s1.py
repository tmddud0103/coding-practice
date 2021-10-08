import sys
sys.stdin = open('input.txt')
from collections import deque
TC = int(input())

for tc in range(1, TC + 1):
    maxnum = 100001
    stack = [0] * (maxnum+1)
    N, K = list(map(int, input().split()))
    q = deque()
    q.append(N)
    while len(q) >0:
        x = q.popleft()
        if x == K:
            print(stack[x])
            break
        for a in (x-1, x+1, x*2):
            if 0 <= a <= maxnum and stack[a] == 0:
                stack[a] = stack[x] + 1
                q.append(a)

