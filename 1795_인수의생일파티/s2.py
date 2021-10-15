import sys
sys.stdin = open('input.txt')

def dijkstra(s, V):
    U = [0] * (V + 1)
    U[s] = 1
    for v in range(V + 1):
        if v != s:
            D[v] = mat[s][v]
    # while len(U) != V:
    for _ in range(V):  # V = 정점개수-1과 같으므로..남은 정점개수와 같음
        minV = INF
        w = 0
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1  # 선택된 집합에 포함

        for v in range(V + 1):  # 정점 v가
            if 0 < mat[w][v] < INF:  # w에 인접이면 , 시작정점에서 w를 거쳐 v로 가능 비용과
                D[v] = min(D[v], D[w] + mat[w][v])

def dijkstra2(s, V):
    U = [0] * (V + 1)
    U[s] = 1
    for v in range(V + 1):
        if v != s:
            D2[v] = mat2[s][v]
    # while len(U) != V:
    for _ in range(V):  # V = 정점개수-1과 같으므로..남은 정점개수와 같음
        minV = INF
        w = 0
        for i in range(V + 1):
            if U[i] == 0 and minV > D2[i]:
                minV = D2[i]
                w = i
        U[w] = 1  # 선택된 집합에 포함

        for v in range(V + 1):  # 정점 v가
            if 0 < mat2[w][v] < INF:  # w에 인접이면 , 시작정점에서 w를 거쳐 v로 가능 비용과
                D2[v] = min(D2[v], D2[w] + mat2[w][v])

TC = int(input())
INF = 100000
for tc in range(1, TC + 1):
    n, m, x = list(map(int, input().split()))
    mat = [[INF]*(n+1) for _ in range(n+1)]
    mat2 = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        mat[i][i] = 0
        mat2[i][i] = 0
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        mat[a][b] = c
        mat2[b][a] = c

    D = [0]*(n+1)
    dijkstra(x, n)
    D[0] = 0
    D2 = [0] * (n + 1)
    total = 0
    # print(D)
    dijkstra2(x, n)
    # print(D2)
    for i in range(1, n+1):
        if total < D[i]+D2[i]:
            total = D[i]+D2[i]

    print('#{} {}'.format(tc, total))