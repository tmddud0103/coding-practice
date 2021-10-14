import sys
from collections import deque
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    n, m = list(map(int, input().split()))
    q=deque([n])
    l = [0]*1000001
    while q:
        a= q.popleft()

        if a == m:
            answer = l[a]
            break
        else:
            if a<1000000 and l[a+1]==0:
                q.append(a+1)
                l[a + 1] = l[a] +1
            if a*2<=1000000 and l[a*2]== 0 :
                q.append(a * 2)
                l[a * 2] =l[a] +1
            if a-1>0 and l[a-1]==0:
                q.append(a - 1)
                l[a -1] = l[a] + 1
            if a-10 > 0 and l[a-10]==0:
                q.append(a - 10)
                l[a -10] = l[a] + 1
    print('#{} {}'.format(tc, answer))