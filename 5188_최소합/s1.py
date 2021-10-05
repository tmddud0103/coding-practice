import sys
sys.stdin = open('sample_input.txt')

def min_total(r, c, total):
    global matrix, N, r_total
    if total > r_total:
        return
    if r < N-1:
        min_total(r+1, c, total+matrix[r+1][c])
    if c < N-1:
        min_total(r, c + 1, total + matrix[r][c + 1])
    if r == N-1 and c == N-1:
        if total < r_total:
            r_total = total
            return 0



TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    r_total = 10 * N
    min_total(0, 0, matrix[0][0])
    print('#{} {}'.format(tc, r_total))