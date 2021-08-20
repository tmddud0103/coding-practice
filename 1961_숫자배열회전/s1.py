import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    matrix = []
    N = int(input())
    for i in range(N):
        mat_row = list(map(int, input().split()))
        matrix.append(mat_row)
    mat90 = [[0 for _ in range(N)] for _ in range(N)]
    mat180 = [[0 for _ in range(N)] for _ in range(N)]
    mat270 = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            mat180[i][j] = matrix[N - 1 - i][N - 1 - j]
            mat90[i][j] = matrix[N -1 -j][i]
            mat270[i][j] = matrix[j][N -1 -i]
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(mat90[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(mat180[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(mat270[i][j], end='')
        print()