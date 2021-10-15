import sys
sys.stdin = open('s_input.txt')

def chch(i):

    for j in range(1, n+1):
        if mat[i][j]==1 and check[j]==0:
            check[j] = 1
            chch(j)


TC = int(input())

for tc in range(1, TC + 1):
    n, m  = list(map(int, input().split()))
    mat = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = list(map(int, input().split()))
        mat[a][b] = 1
        mat[b][a] = 1
    check = [0]*(n+1)
    check[0] = 1
    total = 0
    for i in range(1, n+1):
        if check[i]==0:
            total+=1
            chch(i)
    print('#{} {}'.format(tc, total))