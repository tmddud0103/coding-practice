import sys
sys.stdin = open('input.txt')
test_case = int(input())

for tc in range(1, test_case + 1):
    length_of_matrix = int(input())
    total_matrix = []
    result = 0
    for row in range(length_of_matrix):
        row_of_matric = list(map(int, input().split()))
        total_matrix += [row_of_matric]

    for i in range(0, length_of_matrix):
        for j in range(0, length_of_matrix):
            if i == 0:
                if j == 0:
                    result += abs(total_matrix[i][0] - total_matrix[0][1]) + abs(total_matrix[0][0] - total_matrix[1][0])
                elif j == length_of_matrix - 1:
                    result += abs(total_matrix[i][j] - total_matrix[0][j - 1]) + abs(total_matrix[0][j] - total_matrix[1][j])
                else:
                    result += abs(total_matrix[i][j] - total_matrix[i + 1][j]) + abs(total_matrix[i][j] - total_matrix[i][j + 1]) + abs(total_matrix[i][j] - total_matrix[i][j - 1])
            elif i == length_of_matrix - 1:
                if j == 0:
                    result += abs(total_matrix[i][j] - total_matrix[i - 1][j]) + abs(total_matrix[i][j] - total_matrix[i][j + 1])
                elif j == length_of_matrix - 1:
                    result += abs(total_matrix[i][j] - total_matrix[i - 1][j]) + abs(total_matrix[i][j] - total_matrix[i][j - 1])
                else:
                    result += abs(total_matrix[i][j] - total_matrix[i - 1][j]) + abs(total_matrix[i][j] - total_matrix[i][j + 1]) + abs(total_matrix[i][j] - total_matrix[i][j - 1])
            else:
                if j == 0:
                    result += abs(total_matrix[i][j] - total_matrix[i - 1][j]) + abs(total_matrix[i][j] - total_matrix[i][j + 1]) + abs(total_matrix[i][j] - total_matrix[i + 1][j])
                elif j == length_of_matrix - 1 :
                    result += abs(total_matrix[i][j] - total_matrix[i - 1][j]) + abs(total_matrix[i][j] - total_matrix[i + 1][j]) + abs(total_matrix[i][j] - total_matrix[i][j - 1])
                else:
                    result += abs(total_matrix[i][j] - total_matrix[i + 1][j]) + abs(total_matrix[i][j] - total_matrix[i - 1][j]) \
                     + abs(total_matrix[i][j] - total_matrix[i][j - 1]) + abs(total_matrix[i][j] - total_matrix[i][j + 1])
    print('#{} {}'.format(tc, result))