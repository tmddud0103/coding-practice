N = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
n = 7

def dfs(k):
    global mat, N, n
    print(k, end='-')
    for i in range(n+1):
        if mat[k][i]==1 and check[i] == 0:
            check[i] = check[k] + 1
            dfs(i)

check = [0]*(n+1)
mat = [[0]*(n+1) for _ in range(n+1)]
for i in range(len(N)//2):
    mat[N[i*2]][N[i*2+1]] = 1
    mat[N[i * 2+1]][N[i * 2]] = 1
check[1] = 1
dfs(1)