import sys
from collections import deque
sys.stdin = open('input.txt')

def ans():
    for i in range(ll):
        for j in range(m):
            if mat[i][j] == 0:
                print(-1)
                return
    if mat[a][b] == -1:
        print(0)
    else:
        print(mat[a][b]-1)

m, n, h = list(map(int, sys.stdin.readline().split()))
ll=n*h
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(ll)]

q = deque()
a, b = 0, 0
for i in range(ll):
    for j in range(m):
        if mat[i][j] == 1:
            q.append([i, j])
x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
while q:
    a, b = q.popleft()
    for i in range(4):
        if 0<=a%n+x[i]<n and 0<=b+y[i]<m and mat[a+x[i]][b+y[i]]==0:
            mat[a + x[i]][b + y[i]] = mat[a][b]+1
            q.append([a + x[i], b + y[i]])
    if 0<=a-n<ll and mat[a-n][b]==0:
        mat[a - n][b] = mat[a][b]+1
        q.append([a-n, b])
    if 0<=a+n<ll and mat[a+n][b]==0:
        mat[a + n][b] = mat[a][b]+1
        q.append([a+n, b])
ans()
