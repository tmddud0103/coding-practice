import sys
sys.stdin = open('input.txt')
# 미로의 거리 복붙 개꿀

def miro(r, c):
    global matrix, d_stack
    # stack.append([r, c])
    # d_stack += 1
    while stack:
        r, c = stack[0]
        if r == end[0] and c == end[1]:
            return d_stack-1

        if r != 0 and matrix[r-1][c] == 0:
            k = 1
            while r - k != -1 and matrix[r-k][c] == 0:
                matrix[r - k][c] = 1
                stack.insert(0, [r-k, c])
                d_stack += 1
                k += 1

        elif r != 16-1 and matrix[r+1][c] == 0:
            k = 1
            while r + k!= 16 and matrix[r+k][c] == 0:
                matrix[r + k][c] = 1
                stack.insert(0, [r+k, c])
                d_stack += 1
                k += 1
        elif c != 0 and matrix[r][c-1] == 0:
            k = 1
            while c - k!= -1 and matrix[r][c-k] == 0:
                matrix[r][c - k] = 1
                stack.insert(0, [r, c-k])
                d_stack += 1
                k += 1
        elif c != 16 - 1 and matrix[r][c+1] == 0:
            k = 1
            while c + k != 16  and matrix[r][c + k] == 0:
                matrix[r][c + k] = 1
                stack.insert(0, [r, c+k])
                k += 1
                d_stack += 1
        else:
            stack.pop(0)
            d_stack -= 1
    return 0




for tc in range(1, 11):
    TC = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    # 시작, 끝 확인
    for i in range(0, 16):
        for j in range(0, 16):
            if matrix[i][j] == 2:
                start = [i, j]
                matrix[i][j] = 1
            if matrix[i][j] == 3:
                end = [i, j]
                matrix[i][j] = 0
    stack = [start]
    d_stack = 0
    a = miro(start[0], start[1])
    if a >0:
        a = 1
    print('#{} {}'.format(TC, a))