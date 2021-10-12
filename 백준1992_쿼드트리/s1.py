import sys
sys.stdin = open('input.txt')

def divide(n, x, y):
    global mat, ans

    init = mat[x][y]
    for i in range(x, n+x):
        a = 0
        for j in range(y, y+n):
            if mat[i][j] != init:
                a = 1
                break
        if a == 1:
            break
    if a == 0:
        ans += str(init)
    else:
        ans += '('
        divide(n//2, x, y)

        divide(n // 2, x, y + n // 2)

        divide(n // 2, x + n // 2, y)

        divide(n // 2, x + n // 2, y + n // 2)
        ans += ')'




n = int(sys.stdin.readline().lstrip())
mat = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
print(mat)
ans = ''
divide(n, 0, 0)
print(ans)