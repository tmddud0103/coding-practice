import sys
sys.stdin = open('input.txt')

T = int(input())
def check_mat():
    global matrix
    for i in range(0, len(matrix)):
        check_row = [0] * 10
        check_col = [0] * 10
        # check_row[0] = check_col[0] = 1
        for j in range(0, 9):
            check_row[matrix[i][j]] += 1
            check_col[matrix[j][i]] += 1
        for k in range(1, 9):
            if check_row[k] != 1 or check_col[k] != 1:
                return 0
    for i in range(0, 3):
        check_sq1 = [0] * 10
        check_sq2 = [0] * 10
        check_sq3 = [0] * 10
        for j in range(0, 3):
            for k in range(0, 3):
                check_sq1[matrix[k][3 * i + j]] += 1
                check_sq2[matrix[k + 3][3 * i + j]] += 1
                check_sq3[matrix[k + 6][3 * i + j]] += 1
        for m in range(1, 9):
            # if (check_sq1[m] != 1) or (check_sq2[m] != 1):
            #     return 0
            # if check_sq3[m] != 1:
            #     return 0
            if (check_sq1[m] != 1) or (check_sq2[m] != 1) or (check_sq3[m] != 1):
                # print(check_sq1)
                # print(check_sq2)
                # print(check_sq3)
                return 0
    return 1

for tc in range(1, T + 1):
    matrix = []
    for i in range(0, 9):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(f'#{tc} {check_mat()}')

