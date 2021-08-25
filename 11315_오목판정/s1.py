import sys
sys.stdin = open('input.txt')

test_case = int(input())

def five():
    for i in range(0, N):
        for j in range(0, N):
            if matrix[i][j] == 'o':
                if j+4 < N and matrix[i][j+1] == 'o' and matrix[i][j+2] == 'o' and matrix[i][j+3] == 'o' and matrix[i][j+4] == 'o':
                    return 'YES'
                if i+4 < N and j+4 < N and matrix[i+1][j+1] == 'o' and matrix[i+2][j+2] == 'o' and matrix[i+3][j+3] == 'o' and matrix[i+4][j+4] == 'o':
                    return 'YES'
                if i+4 < N and j-4 >= 0 and matrix[i+1][j-1] == 'o' and matrix[i+2][j-2] == 'o' and matrix[i+3][j-3] == 'o' and matrix[i+4][j-4] == 'o':
                    return 'YES'
                if i + 4 < N and matrix[i+1][j] == 'o' and matrix[i+2][j] == 'o' and matrix[i+3][j] == 'o' and matrix[i+4][j] == 'o':
                    return 'YES'

            # if matrix[j][i] == 'o':
            #     if matrix[j+1][i] == 'o' and matrix[j+2][i] == 'o' and matrix[j+3][i] == 'o' and matrix[j+4][i] == 'o':
            #         return 'YES'
            # if matrix[j][j] == 'o':
            #     if matrix[j + 1][j + 1] == 'o' and matrix[j + 2][j + 2] == 'o' and matrix[j + 3][j + 3] == 'o' and matrix[j + 4][j + 4] == 'o':
            #         return 'YES'
            # if matrix[j][N-1-j]  == 'o':
            #     if matrix[j + 1][N-2-j] == 'o' and matrix[j + 2][N-3-j] == 'o' and matrix[j + 3][N-4-j] == 'o' and matrix[j + 4][N-5-j] == 'o':
            #         return 'YES'
    return 'NO'


for tc in range(1, test_case + 1):
    N = int(input())
    matrix = []
    for i in range(N):
        temp = list(map(str, input()))
        matrix.append(temp)
    print('#{} {}'.format(tc, five()))

