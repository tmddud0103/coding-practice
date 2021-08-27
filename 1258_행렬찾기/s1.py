import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    num_of_matrix = 0
    c_r = []
    c_mul_r = []
    mun = 0
    for i in range(N):
        for j in range(N):
            c = 0
            r = 0
            if matrix[i][j] != 0:
                while (j + c != N) and (matrix[i][j + c] != 0):
                    # matrix[i][j + c] = 0
                    c += 1
                while (i + r != N) and (matrix[i + r][j] != 0):
                    r += 1
                c_r.append([r, c])
                c_mul_r.append([c*r, mun])
                mun += 1
                for k in range(c):
                    for l in range(r):
                        matrix[i+l][j+k] = 0
    # print(c_r, c_mul_r)
    print('#{} {}'.format(tc, len(c_r)), end =' ')
    while c_mul_r:
        area, num = c_mul_r.pop()
        for i in range(len(c_mul_r)):
            if area > c_mul_r[i][0]:
                [area, num], c_mul_r[i] = c_mul_r[i], [area, num]
            if area == c_mul_r[i][0]:
                if c_r[num][0] > c_r[c_mul_r[i][1]][0]:
                    [area, num], c_mul_r[i] = c_mul_r[i], [area, num]
        print(c_r[num][0], c_r[num][1], end=' ')
    print()