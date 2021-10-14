import sys
sys.stdin = open('sample_input.txt')

def mst_print(start, mat):
    global v
    key = [1000000] *(v+1)
    key[0] = 0
    mst = [0] * (v + 1)
    pi = [0] * (v + 1)
    for _ in range(v):
        u = 0
        minv = 10000000
        for i in range(v+1):
            if mst[i]==0:
                if key[i]<minv:
                    u = i
                    minv = key[i]
        mst[u] = 1
        for v in range(v+1):
            if mst[v]==0 and mat[u][v] !=0:
                if key[v] > mat[u][v]:
                    key[v] = mat[u][v]
                    pi[v] = u
    return sum(key[start:])

TC = int(input())

for tc in range(1, TC+1):
    v, e = list(map(int, input().split()))
    mat = [[0]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        i, j, k = list(map(int, input().split()))
        mat[i][j], mat[j][i] = k, k
    print('#{} {}'.format(tc, mst_print(0, mat)))