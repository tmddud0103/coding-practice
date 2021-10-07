import sys
sys.stdin = open('input.txt')

def go_bug(que):
    global mat, M, N, cnt
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]
    while que:
        a, b = que.pop()
        for i in range(4):
            if 0 <= a+x[i] < M and 0 <= b+y[i] < N:
                if mat[a+x[i]][b+y[i]] == 1:
                    mat[a + x[i]][b + y[i]] = 0
                    que.append([a + x[i], b + y[i]])
    cnt += 1


TC = int(sys.stdin.readline().rstrip())
for tc in range(TC):
    M, N, K = list(map(int, sys.stdin.readline().split()))
    mat = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x, y = list(map(int, sys.stdin.readline().split()))
        mat[x][y] = 1
    que = []
    cnt = 0
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1:
                que.append([i, j])
                go_bug(que)
    print(cnt)