import sys
sys.stdin = open('input.txt')



TC = int(input())
for tc in range(1, TC+1):
    N, M, L = list(map(int, input().split()))
    tree = [0 for _ in range(N + 1)]
    for _ in range(M):
        k, n = list(map(int, input().split()))
        tree[k] = n
    if N % 2 == 0:
        tree[N//2] = tree[N]
        N -= 1
    while N != 1:
        tree[N//2] = tree[N] + tree[N-1]
        N -= 2
    print(f'#{tc} {tree[L]}')