import sys
from collections import deque
sys.stdin = open('sample_input.txt')

def drive():
    global mat, x, y, n, mat2
    q = deque([[0,0]])
    while q:
        i, j = q.popleft()
        for k in range(4):
            a = i + x[k]
            b = j + y[k]
            if 0<=a<n and 0<=b<n:
                if mat[i][j] < mat[a][b] and mat2[i][j]-mat[i][j]+mat[a][b]+1 <mat2[a][b]:
                    mat2[a][b] = mat2[i][j]-mat[i][j]+mat[a][b]+1
                    q.append([a, b])
                elif mat[i][j] >= mat[a][b] and mat2[i][j]+1 < mat2[a][b]:
                    mat2[a][b] = mat2[i][j] + 1
                    q.append([a, b])
                else:
                    pass

TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    #    하 우 상 좌
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    total = 98765432101
    mat2 = [[total]*(n) for _ in range(n)]
    mat2[0][0] = 0
    drive()
    print('#{} {}'.format(tc, mat2[n-1][n-1]))