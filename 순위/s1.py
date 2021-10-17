def solution(n, results):
    answer = 0
    mat = [[0]*(n+1) for _ in range(n+1)]
    cntw = [0]*(n+1)
    cntl = [0]*(n+1)
    for re in results:
        mat[re[0]][re[1]] = 1
    for i in range(1, n+1):
        q = []
        check = [0]*(n+1)
        for j in range(1, n+1):
            if mat[i][j]==1:
                q.append(j)
                cntw[i]+=1
                cntl[j]+=1
                check[j] = 1
        while q:
            a = q.pop()
            for j in range(1, n+1):
                if mat[a][j] == 1 and check[j]==0:
                    check[j]=1
                    q.append(j)
                    cntw[i]+=1
                    cntl[j]+=1
    print(cntw)
    print(cntl)
    for i in range(1, n+1):
        if cntw[i]+cntl[i] == n-1:
            answer+=1
    return answer