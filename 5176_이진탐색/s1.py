import sys
sys.stdin = open('input.txt')

def search(n):
    global K
    if 2*n+1 <= N:
        search(2*n+1)
    tree[n] = K
    K -= 1
    if 2*n <= N:
        search(2*n)
    return 0


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    K = N
    tree = [0 for _ in range(N+1)]
    search(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')