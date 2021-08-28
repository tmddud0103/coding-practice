import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    total = 0
    for i in range(N//2+1):
        total += farm[i][N//2]
        for j in range(1, i+1):
            total += farm[i][N//2 + j]
            total += farm[i][N//2 - j]
            # print(farm[i][N//2 + j], farm[i][N//2 - j])
    for i in range(N//2+1, N):
        total += farm[i][N // 2]
        for j in range(1, N-i):
            total += farm[i][N // 2 + j]
            total += farm[i][N // 2 - j]
            # print(farm[i][N // 2 + j], farm[i][N // 2 - j])
    print('#{} {}'.format(tc, total))