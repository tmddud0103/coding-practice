import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    matrix = []
    matrix_col = []
    for i in range(1, 6):
        temp = list(map(str, input()))
        matrix.append(temp)
    print(f'#{tc}', end=' ')
    for i in range(0, 16):
        temp_mat = []
        for j in range(0, 6):
            try:
                # temp_mat.append(matrix[j][i])
                print(matrix[j][i], end='')
            except:
                pass
    #     matrix_col.append([temp_mat])
    # print(matrix_col)
    print()