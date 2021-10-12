import sys
sys.stdin = open('sample_input.txt')
def dessertcafe(i, j, a, cnt):
    global check, mat, n, x, y, total, kcheck, checkpoint
    # print(check)
    if a==-1:
        nx = i + x[0]
        ny = j + y[0]
        if 0 <= nx < n and 0 <= ny < n:
            if check[mat[nx][ny]] == 0:
                check[mat[nx][ny]] = 1
                kcheck[0] += 1
                dessertcafe(nx, ny, 0, cnt+1)
                check[mat[nx][ny]] = 0
                kcheck[0] -= 1
    elif a==0:
        for k in range(0, 2):
            nx = i + x[k]
            ny = j + y[k]
            if 0 <= nx < n and 0 <= ny < n:
                if check[mat[nx][ny]] == 0:
                    check[mat[nx][ny]] = 1
                    kcheck[k] += 1
                    dessertcafe(nx, ny, k, cnt + 1)
                    check[mat[nx][ny]] = 0
                    kcheck[k] -= 1
    elif a==1:
        for k in range(a, 3):
            nx = i + x[k]
            ny = j + y[k]
            if 0 <= nx < n and 0 <= ny < n:
                if check[mat[nx][ny]] == 0:
                    check[mat[nx][ny]] = 1
                    kcheck[k] += 1
                    dessertcafe(nx, ny, k, cnt + 1)
                    check[mat[nx][ny]] = 0
                    kcheck[k] -= 1
    else:
        if kcheck[2] > kcheck[0]:
            return
        if kcheck[3] > kcheck[1]:
            return
        # print(total, kcheck)
        if kcheck[0] + kcheck[1] <total//2:
            return
        for k in range(a, 4):
            nx = i + x[k]
            ny = j + y[k]
            if 0<=nx<n and 0<=ny<n:
                if check[mat[nx][ny]]==0:
                    check[mat[nx][ny]] = 1
                    kcheck[k] += 1
                    dessertcafe(nx, ny, k, cnt + 1)
                    check[mat[nx][ny]] = 0
                    kcheck[k] -= 1
                elif check[mat[nx][ny]]==2 and k==3 and checkpoint == [nx, ny]:
                    # and checkpoint == [nx, ny]
                    if cnt > total:
                        if kcheck[0]==kcheck[2] and kcheck[1]==kcheck[3]+1:
                            # print(check, cnt, nx, ny, kcheck)
                            total = cnt
                    return
                else:
                    return

TC = int(input())

for tc in range(1, TC + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    check = [0]*101
    #       반시계
    # 좌하,우하,우상,좌상
    x = [1, 1, -1, -1]
    y = [-1, 1, 1, -1]
    kcheck = [0, 0, 0, 0]
    total = -1
    for i in range(0, n-2):
        for j in range(1, n-1):
            checkpoint = [i, j]
            check[mat[i][j]] = 2
            dessertcafe(i, j, -1, 1)
            check[mat[i][j]] = 0
    print('#{} {}'.format(tc, total))