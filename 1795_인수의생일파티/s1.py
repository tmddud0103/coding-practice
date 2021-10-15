import sys
sys.stdin = open('input.txt')

def F_W():
    for k in range(1, n+1):
        mat[k][k] = 0
        for i in range(1, n + 1):
            if i == k:
                continue
            # if mat[i][k] == INF:
            #     continue
            for j in range(1, n + 1):
                # if i == j:
                #     continue
                # if j == k:
                #     continue
                if mat[i][j] > mat[i][k] + mat[k][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]


TC = int(input())

for tc in range(1, TC + 1):
    INF = 100000
    n, m, x = list(map(int, input().split()))
    mat = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        mat[a][b] = c
    # for i in range(n+1):
    #     mat[i][i]=0
    F_W()
    # print(mat)
    total = mat[1][x]+mat[x][1]
    for i in range(2, n+1):
        if total < mat[i][x]+mat[x][i]:
            total = mat[i][x]+mat[x][i]

    print('#{} {}'.format(tc, total))