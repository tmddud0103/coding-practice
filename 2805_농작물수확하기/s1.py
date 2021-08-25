import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    mat = []
    for _ in range(N):
        temp = list(map(int, input()))
        mat.append(temp)
    center = N//2
    k = 0
    total = mat[0][center]
    for i in range(1, N//2+1):
        k += 1
        total += mat[i][center]
        for j in range(1, k+1):
            total += mat[i][center-j]
            total += mat[i][center+j]
    for i in range(N//2+1, N):
        k -= 1
        total += mat[i][center]
        for j in range(1, k+1):
            total += mat[i][center-j]
            total += mat[i][center+j]
    print('#{} {}'.format(tc, total))
