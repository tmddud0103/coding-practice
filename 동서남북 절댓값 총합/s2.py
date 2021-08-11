import sys
sys.stdin = open('input.txt')
test_case = int(input())

# 각각 행렬을 집어넣고 위,아래,오른,왼쪽의 값이랑 뺀 값을 반환단다
# 만약 위,아래,오른,왼쪽의 값지 존재하지 않다면 0을 반환한다
def up(matrix, i, j, length):
    if i == 0:
        return 0
    return abs(matrix[i][j] - matrix[i - 1][j])
def down(matrix, i, j, length):
    if i == length - 1:
        return 0
    return abs(matrix[i][j] - matrix[i + 1][j])
def left(matrix, i, j, length):
    if j == 0:
        return 0
    return abs(matrix[i][j] - matrix[i][j - 1])
def right(matrix, i, j, length):
    if j == length - 1:
        return 0
    return abs(matrix[i][j] - matrix[i][j + 1])

for tc in range(1, test_case + 1):
    length_of_matrix = int(input())
    total_matrix = []
    result = 0
    for row in range(length_of_matrix):
        row_of_matric = list(map(int, input().split()))
        total_matrix += [row_of_matric]
    for i in range(0, length_of_matrix):
        for j in range(0, length_of_matrix):
            result += up(total_matrix, i, j, length_of_matrix) + down(total_matrix, i, j, length_of_matrix) + right(total_matrix, i, j, length_of_matrix) + left(total_matrix, i, j, length_of_matrix)
    print('#{} {}'.format(tc, result))