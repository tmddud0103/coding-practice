import sys
sys.stdin = open('input.txt')

def del_h(g, i, j):
    global mat
    a = [1, -1, 0, 0, 2, -2, 0, 0, 3, -3, 0, 0]
    b = [0, 0, 1, -1, 0, 0, 2, -2, 0, 0, 3, -3]
    if g == 'A':
        for k in range(0, 4):
            if i + a[k] > -1 and j + b[k] > -1 and i + a[k] < N and j + b[k] < N :
                if mat[i + a[k]][j + b[k]] == 'H':
                    mat[i + a[k]][j + b[k]] = 'X'
    if g == 'B':
        for k in range(0, 8):
            if i + a[k] > -1 and j + b[k] > -1 and i + a[k] < N and j + b[k] < N :
                if mat[i + a[k]][j + b[k]] == 'H':
                    mat[i + a[k]][j + b[k]] = 'X'
    if g == 'C':
        for k in range(0, 12):
            if i + a[k] > -1 and j + b[k] > -1 and i + a[k] < N and j + b[k] < N :
                if mat[i + a[k]][j + b[k]] == 'H':
                    mat[i + a[k]][j + b[k]] = 'X'



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    mat = [list(map(str, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'A':
                del_h('A', i, j)
            elif mat[i][j] == 'B':
                del_h('B', i, j)
            elif mat[i][j] == 'C':
                del_h('C', i, j)
            else:
                pass
    count = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'H':
                count += 1

    print('#{} {}'.format(tc, count))
