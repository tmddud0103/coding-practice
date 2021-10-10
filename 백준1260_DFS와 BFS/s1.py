import sys
sys.stdin = open('input.txt')

def dfs(st):
    global n, mat, check
    for i in range(n+1):
        if mat[st][i] == 1 and check[i] == 0:
            check[i] = 1
            print(i, end=" ")
            dfs(i)

def bfs(st):
    global n, mat, check
    q = [st]
    print(st, end =" ")
    while q:
        a = q.pop(0)
        for i in range(n + 1):
            if mat[a][i] == 1 and check[i] == 0:
                check[i] = 1
                print(i, end=" ")
                q.append(i)
    print()


n, m, s = list(map(int, sys.stdin.readline().split()))
mat = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = list(map(int, sys.stdin.readline().split()))
    mat[x][y], mat[y][x] = 1, 1
check = [0] * (n+1)
check[s] = 1
print(s, end =" ")
dfs(s)
print()
check = [0] * (n+1)
check[s] = 1
bfs(s)