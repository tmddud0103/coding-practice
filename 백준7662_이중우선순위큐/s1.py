import sys
import heapq
sys.stdin = open('input.txt')


TC = int(sys.stdin.readline().lstrip())
for _ in range(TC):
    heap = []
    maxheap = []
    ins = 0
    dele = 0
    n = int(sys.stdin.readline().lstrip())
    for _ in range(n):
        in_de, num = list(map(str, sys.stdin.readline().split()))
        if in_de == 'I':
            heapq.heappush(heap, int(num))
            heapq.heappush(maxheap, (-0.1 * int(num), num))
            ins += 1
        else:
            dele += 1
            if ins <= dele:
                if ins > 0:
                    heap = []
                    maxheap = []
                    ins = 0
                dele = 0
            else:
                if num == '1':
                    heapq.heappop(maxheap)
                else:
                    heapq.heappop(heap)
    if ins == 0:
        print('EMPTY')
    elif ins - dele == 1:
        print('{} {}'.format(heap[0], heap[0]))
    else:
        print('{} {}'.format(maxheap[0][1], heap[0]))


