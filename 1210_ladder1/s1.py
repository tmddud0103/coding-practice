import sys
sys.stdin = open('input.txt')

# test_case = int(input())
# 10개 테스트 케이스

for tc in range(1, 11):
    x = 0
    matrix = []
    test_case_number = int(input())
    for i in range(100):
        matrix += [list(map(int, input().split()))]
    for i in range(100):
        if matrix[99][i] == 2:
            x = i
    y = 99
    while y > 0:
        if x < 99:
            if matrix[y][x + 1] == 1:
                x += 1
                while matrix[y][x + 1] == 1:
                    matrix[y][x] = 0
                    x += 1
                    if x == 99:
                        break
        if x > 0:
            if matrix[y][x - 1] == 1:
                x -= 1
                while matrix[y][x - 1] == 1:
                    matrix[y][x] = 0
                    x -= 1
                    if x == 0:
                        break
        y -= 1
    print('#{} {}'.format(tc, x))
