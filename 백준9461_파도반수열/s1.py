import sys
sys.stdin = open('input.txt')


TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    N = int(sys.stdin.readline().rstrip())
    k = [0] * (N + 5)
    k[1], k[2], k[3] = 1, 1, 1
    k[4], k[5] = 2, 2
    if N >= 6:
        for i in range(6, N+1):
            k[i] = k[i-1] + k[i-5]
    print(k[N])