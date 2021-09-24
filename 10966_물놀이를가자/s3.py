# 교수님 풀이(통과)
import sys
sys.stdin = open('input.txt')
from collections import deque

   # 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))
    arr = [input() for _ in range(N)]

    dist = [[999999999] * M for _ in range(N)]

    # Q = deque()
    Q = [0] * (N * M)
    front = -1
    rear = -1


    for i in range(N):
        for j in range(M):
            if arr[i][j] =='W':
                rear += 1
                Q[rear] = (i, j)
                # Q.append((i, j))
                dist[i][j] = 0

    while front != rear:
        # r, c = Q.popleft()
        front += 1
        r, c = Q[front]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >=N or nc < 0 or nc >=M: continue
            elif arr[nr][nc] == 'L' and dist[nr][nc] == 999999999:
                dist[nr][nc] = dist[r][c] + 1
                # Q.append((nr,nc))
                rear += 1
                Q[rear] = (nr, nc)
    ans = 0

    for i in dist:
        for j in i:
            ans += j
    print('#{} {}'.format(tc, ans))