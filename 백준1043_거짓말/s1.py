import sys
sys.stdin = open('input.txt')


n, m = list(map(int, sys.stdin.readline().split()))
s = list(map(int, sys.stdin.readline().split()))[1:]
if s == []:
    print(m)
else:
    check = [0]*(n+1)
    for i in range(len(s)):
        check[s[i]] = 1
    mat = []
    for j in range(m):
        temp = [0]*(n+1)
        te = list(map(int, sys.stdin.readline().split()))[1:]
        for k in te:
            temp[k] = 1
        mat.append(temp)
    while s:
        kk = s.pop(0)
        for i in range(m):
            if mat[i][kk] == 1:
                mat[i][0] = 1
                for j in range(1, n+1):
                    if mat[i][j] == 1 and check[j] == 0:
                        s.append(j)
                        check[j] = 1
    ans = 0
    for j in range(m):
        if mat[j][0] == 0:
            ans += 1
    print(ans)
