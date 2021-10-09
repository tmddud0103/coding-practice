import sys
import heapq
sys.stdin = open('input.txt')


TC = int(sys.stdin.readline().lstrip())
for _ in range(TC):
    heap = []
    maxheap = []
    visit = [0]*1000001
    n = int(sys.stdin.readline().lstrip())
    for i in range(n):
        in_de, num = list(map(str, sys.stdin.readline().split()))
        if in_de == 'I':
            heapq.heappush(heap, (int(num), i))
            heapq.heappush(maxheap, (-1 * int(num), i))
            visit[i] = 1
        elif num == '1':
            while maxheap and visit[maxheap[0][1]]==0:
                heapq.heappop(maxheap)
            if maxheap:
                visit[maxheap[0][1]] = 0
                heapq.heappop(maxheap)
        else:
            while heap and visit[heap[0][1]] == 0:
                heapq.heappop(heap)
            if heap:
                visit[heap[0][1]] = 0
                heapq.heappop(heap)
    while maxheap and visit[maxheap[0][1]] == 0:
        heapq.heappop(maxheap)
    while heap and visit[heap[0][1]] == 0:
        heapq.heappop(heap)

    else:
        if maxheap and heap:
            print('{} {}'.format(-maxheap[0][0], heap[0][0]))
        else:
            print('EMPTY')