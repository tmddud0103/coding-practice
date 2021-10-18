import sys
sys.stdin = open('input.txt')

def asd(i, j, temp, cnt):
    global x, y, maxtotal, mat, n, m
    if cnt == 4:
        if maxtotal<temp:
            maxtotal = temp
        return
    for kl in range(3):
        nx = i+x[kl]
        ny = j+y[kl]
        if 0<=nx<n and 0<=ny<m and mat[nx][ny]!=0:
            l = mat[nx][ny]
            mat[nx][ny] = 0
            asd(nx, ny, temp+l, cnt+1)
            mat[nx][ny] = l

def asd2(i, j):
    global mat, maxtotal, n, m
    if 0<=i<n-1 and 0<j<m-1:
        temp = mat[i][j]+mat[i+1][j]+mat[i][j-1]+mat[i][j+1]
        if temp > maxtotal:
            maxtotal = temp
        temp = mat[i][j]+mat[i+1][j]+mat[i+1][j-1]+mat[i+1][j+1]
        if temp > maxtotal:
            maxtotal = temp
    if 0<=i<n-2 and 0<=j<m-1:
        temp = mat[i][j] + mat[i + 1][j] + mat[i+2][j] + mat[i+1][j + 1]
        if temp > maxtotal:
            maxtotal = temp
    if 0<=i<n-2 and 0<j<m:
        temp = mat[i][j] + mat[i + 1][j] + mat[i + 2][j] + mat[i + 1][j - 1]
        if temp > maxtotal:
            maxtotal = temp

n, m = list(map(int, sys.stdin.readline().split()))

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
x = [-1, 0, 0]
y = [0, 1, -1]
maxtotal = 0
for i in range(n):
    for j in range(m):
        k = mat[i][j]
        mat[i][j] = 0
        asd(i, j, k, 1)
        mat[i][j] = k
        asd2(i, j)
print(maxtotal)
