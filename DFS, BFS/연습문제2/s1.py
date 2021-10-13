N = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
n = 7

def bfs(k):
    global mat, n, N, check
    q = [k]
    while q:
        asd = q.pop(0)
        print(asd, end='-')
        for i in range(n+1):
            if mat[asd][i]==1 and check[i]==0:
                check[i] = 1
                q.append(i)



check = [0]*(n+1)
mat = [[0]*(n+1) for _ in range(n+1)]
for i in range(len(N)//2):
    mat[N[i*2]][N[i*2+1]] = 1
    mat[N[i * 2+1]][N[i * 2]] = 1
check[1] = 1
bfs(1)