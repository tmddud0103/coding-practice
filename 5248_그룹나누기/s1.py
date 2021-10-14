import sys
sys.stdin = open('sample_input.txt')

def dfs(a):
    for i in range(1,n+1):
        if mat[a][i]==1 and ch[i]==0:
            ch[i] = 1
            dfs(i)

TC = int(input())

for tc in range(1, TC+1):
    answer = 0
    n, m = list(map(int, input().split()))
    ll = list(map(int, input().split()))
    mat = [[0]*(n+1) for _ in range(n+1)]
    ch = [0]*(n+1)
    for i in range(len(ll)//2):
        mat[ll[i*2]][ll[i*2+1]], mat[ll[i*2+1]][ll[i*2]] =1, 1
    for i in range(1, n+1):
        if ch[i]==0:
            ch[i]=1
            answer+=1
            dfs(i)

    print('#{} {}'.format(tc, answer))