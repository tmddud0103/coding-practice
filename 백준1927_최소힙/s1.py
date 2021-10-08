import sys
import heapq
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().lstrip())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline().lstrip())
    if x == 0:
        if len(heap)==0:
            print('0')
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)