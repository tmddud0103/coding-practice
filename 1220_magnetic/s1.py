import sys
sys.stdin = open('input.txt')

# 10th
for tc in range(1, 11):
    N = int(input())
    mat = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        mat.append(temp)
    ns = 0
    for i in range(N):
        for j in range(N):
            # 1 = n, 2 = s
            if mat[i][j] == 1:
                k = 1
                if i == 99:
                    mat[i][j] = 0
                else:
                    while i+k != 99 and mat[i+k][j] == 0:
                        k += 1
                    if i+k == 99 and mat[99][j] == 0:
                        mat[i][j] = 0
                    elif mat[i+k][j] == 1:
                        # mat[i + k - 1][j], mat[i][j] = mat[i][j], mat[i+k - 1][j]
                        pass
                    elif mat[i+k][j] == 2:
                        ns += 1
                        # mat[i][j] = 0
                        # mat[i+k][j] = 0

    print('#{} {}'.format(tc, ns))


