#s1은 왜 안될까
import sys
sys.stdin = open('sample_input.txt')

def dessertcafe(i, j, a, cnt):
    global x, y, total, checkpoint
    if a == 4:
        return
    if [i, j] == checkpoint:
        total = max(total, cnt)
        return
    if 0 <= i < n and 0 <= j < n and not check[mat[i][j]]:
        check[mat[i][j]] = 1
        dessertcafe(i + x[a], j + y[a], a, cnt+1)
        dessertcafe(i + x[(a+1)%4], j + y[(a+1)%4], a+1, cnt+1)
        check[mat[i][j]] = 0

TC = int(input())

for tc in range(1, TC + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    check = [0]*101
    #       반시계
    # 좌하,우하,우상,좌상
    x = [1, 1, -1, -1]
    y = [-1, 1, 1, -1]
    total = -1
    for i in range(0, n-2):
        for j in range(1, n-1):
            checkpoint = [i, j]
            check[mat[i][j]] = 1
            dessertcafe(i+1, j-1, 0, 1)
            check[mat[i][j]] = 0
    print('#{} {}'.format(tc, total))