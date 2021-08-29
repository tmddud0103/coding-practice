import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    max_num = -100000
    if N > M:
        n_m = N - M
        length = len(bj)
        for i in range(0, n_m):
            temp = 0
            for j in range(0, length):
                temp += aj[j + i] * bj[j]
            if temp > max_num:
                max_num = temp
    else:
        n_m = M - N
        length = len(aj)
        for i in range(0, n_m+1):
            temp = 0
            for j in range(0, length):
                temp += aj[j] * bj[j + i]
            if temp > max_num:
                max_num = temp
    print(f'#{tc} {max_num}')


