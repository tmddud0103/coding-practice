board =[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
a =[1, 0]
b=[1, 2]

def solution(board, aloc, bloc):
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for d in range(4):
        i = aloc[0]
        j = aloc[1]
        next_i = i + dy[d]
        next_j = j + dx[d]
        if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]):
            if board[next_i][next_j] == 1:
                queue.append([next_i, next_j])
                count[next_i][next_j] = count[i][j] + 1
            if maze[next_i][next_j] == 3:
                return count[i][j]
    return answer

def cycle():


print(solution(board, a, b))