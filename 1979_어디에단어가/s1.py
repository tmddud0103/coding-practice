import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    # N = 행렬 크기
    # K = 원하는 단어의 길이
    N, K = list(map(int, input().split()))
    matrix = []
    for i in range(N):
        matrix += [list(map(int, input().split()))]
    k_count = [0] * (N + 1)
    len_count = 0
    for i in range(N):
        len_count = 0
        for j in range(N):
            if matrix[i][j] == 1:
                len_count += 1
            if matrix[i][j] == 0:
                k_count[len_count] += 1
                len_count = 0
            if j == N - 1:
                k_count[len_count] += 1
                len_count = 0
    for i in range(N):
        len_count = 0
        for j in range(N):
            if matrix[j][i] == 1:
                len_count += 1
            if matrix[j][i] == 0:
                k_count[len_count] += 1
                len_count = 0
            if j == N - 1:
                k_count[len_count] += 1
                len_count = 0
    print('#{} {}'.format(tc, k_count[K]))