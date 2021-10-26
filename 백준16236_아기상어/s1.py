import sys
from collections import deque
sys.stdin = open('input.txt')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N = int(sys.stdin.readline())
mat = [list(map(int, input().split())) for _ in range(N)]
movetime = 0
shark_size = 2
eat = 0
for i in range(0, N):
    for j in range(0, N):
        if mat[i][j] == 9:
            mat[i][j] = 0
            sx = i
            sy = j
            break

while True:
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * N for _ in range(N)]
    flag = 1e9
    fish = []
    while q:
        x, y, count = q.popleft()
        if count > flag:
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0>nx or 0>ny or N<=nx or N<=ny:
                continue
            if mat[nx][ny] > shark_size or visited[nx][ny]:
                continue
            if mat[nx][ny] != 0 and mat[nx][ny] < shark_size:
                fish.append((nx, ny, count+1))
                flag = count
            visited[nx][ny] = True
            q.append((nx, ny, count+1))
    if len(fish)>0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        movetime += move
        eat += 1
        mat[x][y] = 0
        if eat == shark_size:
            shark_size += 1
            eat = 0
        sx, sy = x, y
    else:
        break
print(movetime)