# 온전한 내 풀이(미완)
import sys
sys.stdin = open('input.txt')

#    상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def startWater(n, c, cnt):
    global matrix, check_move
    # print(check_move)

    for i in range(4):
        nr = n + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and (check_move[nr][nc] == -1 or check_move[nr][nc] > cnt):
            cnt += 1
            if cnt > N:
                break
            check_move[nr][nc] = cnt
            startWater(nr,nc, cnt)
            cnt -= 1


TC = int(input())
for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(str, input())) for _ in range(N)]
    check_move = [[-1 for _ in range(M)] for _ in range(N)]
    water = []
    cnt = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                check_move[i][j] = 0
                startWater(i, j, cnt)
    # while water:
    #     start_water = water.pop()
    #     startWater(start_water[0], start_water[1], cnt)
    total = 0
    for i in range(N):
        total += sum(check_move[i])
    print(check_move)
    print('#{} {}'.format(tc, total))