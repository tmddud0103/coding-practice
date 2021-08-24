# 재귀
import sys
sys.stdin = open('input.txt')


def map_around(matrix, start, end):
    global total
    ns = start[:]
    if start == end:
        total = 1
    if start[0] != 0 and matrix[start[0] - 1][start[1]] == 0:
        ns[0] -= 1
        matrix[ns[0]][ns[1]] = 1
        map_around(matrix, ns, end)
    if start[0] != N - 1 and matrix[start[0] + 1][start[1]] == 0:
        ns[0] += 1
        matrix[ns[0]][ns[1]] = 1
        map_around(matrix, ns, end)
    if start[1] != 0 and matrix[start[0]][start[1] - 1] == 0:
        ns[1] -= 1
        matrix[ns[0]][ns[1]] = 1
        map_around(matrix, ns, end)
    if start[1] != N - 1 and matrix[start[0]][start[1] + 1] == 0:
        ns[1] += 1
        matrix[ns[0]][ns[1]] = 1
        map_around(matrix, ns, end)

    if start == end:
        total = 1
        return


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    matrix = []
    for i in range(N):
        temp = list(map(int, input()))
        matrix.append(temp)
    start = []
    end = []
    total = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 3:
                end.append(i)
                end.append(j)
            if matrix[i][j] == 2:
                start.append(i)
                start.append(j)
    matrix[start[0]][start[1]] = 0
    matrix[end[0]][end[1]] = 0
    map_around(matrix, start, end),
    print('#{} {}'.format(tc,  total))