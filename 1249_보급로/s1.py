import sys
from collections import deque
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    n = int(input())
    mat = [list(map(int, input())) for _ in range(n)]
    mat2 = [[99999]*(n) for _ in range(n)]
    mat2[0][0] = 0
    q = deque([[0, 0]])
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    while q:
        # print(q)
        a, b = q.popleft()
        # if a==n-1 and b==n-1:
        #     break
        for i in range(4):
            na = a+x[i]
            nb = b+y[i]
            if 0<=na<n and 0<=nb<n and mat2[na][nb] > mat2[a][b]+mat[na][nb]:
                mat2[na][nb] = mat2[a][b]+mat[na][nb]
                q.append([na, nb])

    print('#{} {}'.format(tc, mat2[n-1][n-1]))