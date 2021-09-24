# 배웠다(완)
# 근데 pop를 쓰면 시간 초과가 나는데 그건 물어봐야겠다
import sys
sys.stdin = open('input.txt')

   # 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))
    matrix = []
    check_move = [[0] * M for _ in range(N)]
    water = []
    cnt = 0
    q = 0
    q_len = 0
    for i in range(N):
        matrix.append(input())
        for j in range(M):
            if matrix[i][j] == 'W':
                water.append((i, j))
                q_len += 1

    while q < q_len:
        r,c = water[q]
        # water.pop()
        #pop를 쓰면 시간 초과가 난다
        q += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 'L' and not check_move[nr][nc]:
                check_move[nr][nc] = check_move[r][c] + 1
                cnt += check_move[nr][nc]
                water.append((nr, nc))
                q_len += 1
    # print(check_move)
    print('#{} {}'.format(tc, cnt))