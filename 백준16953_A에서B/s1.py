import sys
from queue import PriorityQueue
sys.stdin = open('input.txt')
que = PriorityQueue()
n, m = map(int, sys.stdin.readline().split())
que.put([n, 1])
while que:
    a, b = que.get()
    if a == m:
        print(b)
        break
    if a > m:
        print(-1)
        break
    que.put([a*2, b+1])
    que.put([a * 10 + 1, b + 1])
