def solution(m, n, puddles):
    answer = 0
    mat = [[0] * (m + 1) for _ in range(n + 1)]
    mat[1][1] = 1
    for i in range(2, n + 1):
        if [1, i] in puddles:
            continue
        mat[i][1] = mat[i - 1][1]

    for j in range(2, m + 1):
        if [j, 1] in puddles:
            continue
        mat[1][j] = mat[1][j - 1]

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if [j, i] in puddles:
                continue
            mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
    return mat[-1][-1] % 1000000007