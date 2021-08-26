import sys
sys.stdin = open('input.txt')

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

        elif r != N-1 and matrix[r+1][c] == 0:
            k = 1
            while r + k!= N and matrix[r+k][c] == 0:
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
        elif c != N - 1 and matrix[r][c+1] == 0:
            k = 1
            while c + k != N  and matrix[r][c + k] == 0:
                matrix[r][c + k] = 1
                stack.insert(0, [r, c+k])
                k += 1
                d_stack += 1
        else:
            stack.pop(0)
            d_stack -= 1
        print(stack, d_stack)
    return 0



TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    # 시작, 끝 확인
    for i in range(0, N):
        for j in range(0, N):
            if matrix[i][j] == 2:
                start = [i, j]
                matrix[i][j] = 1
            if matrix[i][j] == 3:
                end = [i, j]
                matrix[i][j] = 0
    stack = [start]
    d_stack = 0

    print('#{} {}'.format(tc, miro(start[0], start[1])))