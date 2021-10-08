import sys
sys.stdin = open('input.txt')

def definition(th, r, c, start):
    global mat, max_total, n, max_start
    a = [r, c]
    q = []
    q.append(a)
    if th == 1:
        if r > 0 and mat[r-1][c]==mat[r][c]-1:
            return
        if r < n-1 and mat[r+1][c]==mat[r][c]-1:
            return
        if c > 0 and mat[r][c-1]==mat[r][c]-1:
            return
        if c < n-1 and mat[r][c+1]==mat[r][c]-1:
            return
    while q:
        r, c = q.pop()
        if r > 0 and mat[r-1][c]==mat[r][c]+1:
            q.append([r-1, c])
            th += 1
        if r < n-1 and mat[r+1][c]==mat[r][c]+1:
            q.append([r+1, c])
            th += 1
        if c > 0 and mat[r][c-1]==mat[r][c]+1:
            q.append([r, c-1])
            th += 1
        if c < n-1 and mat[r][c+1]==mat[r][c]+1:
            q.append([r, c+1])
            th += 1
    if th > max_total or (th == max_total and start < max_start):
        max_start = start
        max_total = th
        return
    return

TC = int(input())

for tc in range(1, TC + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    max_total = 0
    max_start = n**2
    for i in range(n):
        for j in range(n):
            definition(1, i, j, mat[i][j])
    print('#{} {} {}'.format(tc, max_start, max_total))