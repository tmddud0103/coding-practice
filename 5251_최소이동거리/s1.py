import sys
sys.stdin = open('sample_input.txt')

def dijkstra(s, v):
    U = [0]*(v+1)
    U[s] = 1
    for i in range(v+1):
        D[i] = mat[s][i]
    for _ in range(v):
        minv = 99999
        w = 0
        for i in range(v+1):
            if U[i]==0 and minv>D[i]:
                minv = D[i]
                w = i
        U[w] = 1
        for j in range(v+1):
            if 0<mat[w][j]<99999:
                D[j] = min(D[j], D[w]+mat[w][j])



TC = int(input())

for tc in range(1, TC+1):
    n, e = list(map(int, input().split()))
    mat = [[99999]*(n+1) for _ in range(n+1)]
    for _ in range(e):
        s, e, w = list(map(int, input().split()))
        mat[s][e] = w
    D = [0] * (n + 1)
    dijkstra(0, n)
    print('#{} {}'.format(tc, D[-1]))