import sys
sys.stdin = open('input.txt')


def find(r, c, N):
    global mat
    for i in range(r, r+N):
        for j in range(c, c+N):

            if mat[r][c] != mat[i][j]:
                return 0
    return 1

def go_quarter(N, r, c):
    global mat, white, blue
    if N == 1:
        if mat[r][c] == 1:
            blue += 1
        else:
            white += 1
        return

    a = find(r, c, N)
    if a == 1:
        if mat[r][c] == 0:
            white += 1
        else:
            blue += 1
        return
    else:
        go_quarter(N // 2, r, c)
        go_quarter(N // 2, r + N // 2, c)
        go_quarter(N // 2, r, c + N // 2)
        go_quarter(N // 2, r + N // 2, c + N // 2)

N = int(sys.stdin.readline().rstrip())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0
go_quarter(N, 0, 0)
print(white)
print(blue)