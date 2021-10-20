import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mat2 = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        mat2[i][j] = mat2[i][j-1] + mat2[i-1][j] - mat2[i-1][j-1] + mat[i-1][j-1]

for _ in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    k = mat2[c][d]
    l = mat2[c][b-1] + mat2[a-1][d] - mat2[a-1][b-1]
    print(k-l)