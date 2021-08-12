import sys
sys.stdin = open('input.txt')


def smashing(x, y, pariche, matrix):
    kill_fly = 0
    for i in range(x, x + pariche):
        for j in range(y, y + pariche):
            kill_fly += matrix[i][j]
    return kill_fly


test_case = int(input())

for tc in range(1, test_case):
    # N = 총 행렬 면적
    # M = 파리채 면적
    N, M = list(map(int, input().split()))
    matrix = []
    for i in range(N):
        matrix += [list(map(int, input().split()))]
    max_kill = 0
    temp = 0
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            temp = smashing(i, j, M, matrix)
            if temp > max_kill:
                max_kill = temp
    print('#{} {}'.format(tc, max_kill))

