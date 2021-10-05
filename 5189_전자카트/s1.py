import sys
sys.stdin = open('sample_input.txt')

def field(r, temp):
    global check_list, total, N, matrix
    if temp > total:
        return 0
    for i in range(N):
        if check_list[i] == 0:
            check_list[i] = 1
            field(i, temp+matrix[r][i])
            check_list[i] = 0
    if sum(check_list)==N and total > temp + matrix[r][0]:
        total = temp + matrix[r][0]
        return 0
    return 0


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    total = 100000
    check_list = [0] * N
    check_list[0] = 1
    field(0, 0)
    print('#{} {}'.format(tc, total))