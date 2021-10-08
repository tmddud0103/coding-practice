import sys
sys.stdin = open('sample_input.txt')

def queen(i):
    global cnt, board, N
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if board[i][j] == 0:
            for k in range(N):
                board[i][k] += 1
                board[k][j] += 1
                if k+i<N and k+j<N:
                    board[i+k][j+k] += 1
                if i-k>-1 and j-k>-1:
                    board[i - k][j - k] += 1
                if i+k<N and j-k>-1:
                    board[i+k][j-k] += 1
            # print(i, board)
            queen(i+1)
            for k in range(N):
                board[i][k] -= 1
                board[k][j] -= 1
                if k + i < N and k + j < N:
                    board[i + k][j + k] -= 1
                if i - k > -1 and j - k > -1:
                    board[i - k][j - k] -= 1
                if i + k < N and j - k > -1:
                    board[i + k][j - k] -= 1

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    board = [[0]* N for _ in range(N)]
    cnt = 0
    queen(0)
    print('#{} {}'.format(tc, cnt))
