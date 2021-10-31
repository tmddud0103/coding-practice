import heapq
def solution(operations):
    heap = []
    maxheap = []
    visit = [0]*1000001
    n = len(operations)
    for i in range(n):
        in_de, num = operations[i].split()
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
    if maxheap and heap:
        answer = [-maxheap[0][0], heap[0][0]]
        return answer
    else:
        return[0, 0]
