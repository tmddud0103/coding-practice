import sys
sys.stdin = open('input.txt')

def miro():
    global stack, matrix, n, m
    a = [-1, 1, 0, 0]
    b = [0, 0, -1, 1]
    while stack:
        x, y = stack.pop(0)
        for i in range(4):
            if 0<=x+a[i]<=n-1 and 0<=y+b[i]<=m-1 and matrix[x+a[i]][y+b[i]] == 1:
                matrix[x + a[i]][y + b[i]] = matrix[x][y] + 1
                stack.append([x + a[i], y + b[i]])
    return matrix[n-1][m-1]

n, m = list(map(int, sys.stdin.readline().split()))
matrix = [list(map(int, input())) for _ in range(n)]
stack = [[0, 0]]
a = miro()

print('{}'.format(a))