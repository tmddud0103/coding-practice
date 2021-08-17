import sys
sys.stdin = open('input.txt')

# test_case = int(input())
for tc in range(1, 11):
    length = int(input())
    matrix = []
    result = 0
    for i in range(8):
        row_matrix = list(map(str, input()))
        matrix.append(row_matrix)
    for i in range(0, 9 - length):
        for j in range(0, 8):
            if matrix[i][j] == matrix[i + length - 1][j]:
                k = 0
                check_num = 0
                while i + k < i + length -1 - k:
                    k += 1
                    if  matrix[ i + k ][j] == matrix[i + length -1 - k][j]:
                        check_num += 1
                if check_num >= length // 2:
                    result += 1
            if matrix[j][i] == matrix[j][i + length - 1]:
                k = 0
                check_num = 0
                while i + k < i + length - 1 - k:
                    k += 1
                    if matrix[j][i + k] == matrix[j][i + length - 1 - k]:
                        check_num += 1
                if check_num >= length // 2:
                    result += 1
    print('#{} {}'.format(tc, result))