# 다른 합격자 풀이 이걸로 좀 배워야겠다(완)
import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = []
    Q = []
    q_len = 0
    for i in range(N):
        arr.append(input())
        for j in range(M):
            if arr[i][j] == 'W':
                Q.append((i, j))
                q_len += 1
    visited = [[0]*M for _ in range(N)]
    ans = 0
    q = 0
    while q < q_len:
        r, c = Q[q]
        q += 1
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                ans += visited[nr][nc]
                Q.append((nr, nc))
                q_len += 1
    print('#{} {}'.format(tc+1, ans))

