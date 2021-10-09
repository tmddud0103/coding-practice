import sys
from collections import deque
sys.stdin = open('input.txt')

def tomato(deq):
    global m, n, mat
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]
    while deq:
        a, b, t = deq.popleft()
        for i in range(4):
            if 0 <= a+x[i] <= n-1 and 0 <= b+y[i] <= m-1:
                if mat[a+x[i]][b+y[i]] == 0:
                    mat[a + x[i]][b + y[i]] = t+1
                    deq.append([a + x[i], b + y[i],t+1])
    return

def maxnum(mat):
    matNumber = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                return -1
            if matNumber < mat[i][j]:
                matNumber = mat[i][j]
    return matNumber-1


m, n = list(map(int, sys.stdin.readline().split()))
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
deq = deque([])
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            deq.append([i, j, 1])
tomato(deq)
print(maxnum(mat))
