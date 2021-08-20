import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    station = [0] * 5001
    N = int(input())
    for n_case in range(1, N + 1):
        S, E = list(map(int, input().split()))
        for i in range(S, E + 1):
            station[i] += 1
    P = int(input())
    print(f'#{tc}', end=' ')
    for p in range(1, P + 1):
        c = int(input())
        print(station[c], end=' ')
    print()