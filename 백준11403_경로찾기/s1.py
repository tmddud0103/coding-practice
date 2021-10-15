import sys
sys.stdin = open('input.txt')

def F_W():
    for k in range( n):
        for i in range( n ):
            if i == k:
                continue
            for j in range( n ):
                if mat[i][k]==1 and mat[k][j]==1:
                    mat[i][j] = 1

n = int(sys.stdin.readline().lstrip())

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
F_W()
for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()
