import sys
sys.stdin = open('input.txt')

def seventhcearch(temp, no, r, c):
    global total, mat
    if no == 7:
        total.add(temp)
        return
    if r > 0:
        seventhcearch(temp + mat[r][c], no+1, r-1, c)
    if r < 3:
        seventhcearch(temp + mat[r][c], no+1, r+1, c)
    if c > 0:
        seventhcearch(temp + mat[r][c], no + 1, r, c-1)
    if c < 3:
        seventhcearch(temp + mat[r][c], no + 1, r, c+1)


TC = int(input())

for tc in range(1, TC + 1):
    mat = [list(map(str, input().split())) for _ in range(4)]
    total = set()
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]
    for i in range(4):
        for j in range(4):
            temp = mat[i][j]
            seventhcearch(temp, 0, i, j)
    print('#{} {}'.format(tc, len(total)))