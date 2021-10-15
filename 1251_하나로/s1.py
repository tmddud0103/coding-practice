import sys
sys.stdin = open('input.txt')
INF = sys.maxsize
def prim(start, V):
    key = [INF]*(V)
    key[0] = 0
    MST = [0]*V
    pi = [0]*V
    for i in range(V):
        u = 0
        minV = INF
        for i in range(V):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        MST[u] = 1
        for v in range(V):
            if MST[v] == 0 and mat[u][v] != 0.0:
                if key[v] > mat[u][v]:  # u를 이용해 기존보다 더 작은 비용으로 MST에 연결된다면
                    key[v] = mat[u][v]
                    pi[v] = u  # v는 u와 연결해서 MST에 포힘될 예정
    return sum(key[start:])

TC = int(input())

for tc in range(1, TC + 1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    mat = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            mat[i][j] = ((x[i]-x[j])**2 + (y[i]-y[j])**2)*E
            mat[j][i] = mat[i][j]

    a = prim(0, n)
    print('#{} {}'.format(tc, round(a)))