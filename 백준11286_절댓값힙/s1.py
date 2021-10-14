import sys
from queue import PriorityQueue
sys.stdin = open('input.txt')
n = int(sys.stdin.readline().lstrip())
q = PriorityQueue()
for _ in range(n):
    a = int(sys.stdin.readline().lstrip())
    if a == 0:
        if q.qsize()==0:
            print(0)
        else:
            # q.sort(key=lambda x:(x[0], x[1]))
            b = q.get()[1]
            print(b)
    else:
        if a<0:
            q.put([abs(a)-0.1, a])
        else:
            q.put([abs(a) + 0.1, a])