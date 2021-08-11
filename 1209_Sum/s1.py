import sys
sys.stdin = open('input.txt')
# test_case = int(input())
#테스트케이스 = 10
for tc in range(1, 11):
    test_number = int(input())
    matrix = []
    max_number = 0
    temp1 = 0
    temp2 = 0
    # 100 * 100 행렬 저장
    for i in range(100):
        row_matrix = list(map(int, input().split()))
        matrix += [row_matrix]
    # 대각선 먼저 빠르게 확인
    for i in range(100):
        max_number += matrix[i][i]
        temp1 += matrix[99 - i][i]
    if temp1 > max_number:
        max_number = temp1
    # 행과 열을 동시에 판단할 수 있을까?
    # 가능 -> i, j의 위치를 반대로 두면 가능하다
    for i in range(100):
        temp1 = 0
        temp2 = 0
        for j in range(100):
            temp1 += matrix[i][j]
            temp2 += matrix[j][i]
        if temp1 > max_number:
            max_number = temp1
        if temp2 > max_number:
            max_number = temp2
    print('#{} {}'.format(tc, max_number))