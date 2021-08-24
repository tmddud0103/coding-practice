# 재귀, while 2가지 방법으로 풀어보기
# while 문으로 풀어보았다...
import sys
sys.stdin = open('input.txt')


def map_around(matrix, start, end):
    stack = [[0]]
    # 스택을 비우기 좀 그래서 [0] 값을 집어넣고
    # 추후에 stack[-1] == [0] 이라면 출구로 못간다
    stack.append(start[:])
    while start != end:
        # 시작을 1으로, 도착지점을 0으로 = 길로 만들어서 도착하도록
        matrix[start[0]][start[1]] = 1
        matrix[end[0]][end[1]] = 0
        # 위
        if start[0] != 0 and matrix[start[0] - 1][start[1]] == 0:
            while start[0] != 0 and matrix[start[0] - 1][start[1]] == 0:
                stack.append(start[:])
                start[0] -= 1
                matrix[start[0]][start[1]] = 1
        # 아래
        elif start[0] != N - 1 and matrix[start[0] + 1][start[1]] == 0:
            while start[0] != N - 1 and matrix[start[0] + 1][start[1]] == 0:
                stack.append(start[:])
                start[0] += 1
                matrix[start[0]][start[1]] = 1
        # 왼
        elif start[1] != 0 and matrix[start[0]][start[1] - 1] == 0:
            while start[1] != 0 and matrix[start[0]][start[1] - 1] == 0:
                stack.append(start[:])
                start[1] -= 1
                matrix[start[0]][start[1]] = 1
        # 오른
        elif start[1] != N - 1 and matrix[start[0]][start[1] + 1] == 0:
            while start[1] != N - 1 and matrix[start[0]][start[1] + 1] == 0:
                stack.append(start[:])
                start[1] += 1
                matrix[start[0]][start[1]] = 1
        #길을 잃었다
        else:
            start = stack.pop()
        # 길이 없다
        if stack[-1] == [0]:
            return 0
    return 1

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    matrix = []
    # matrix = 미로
    for i in range(N):
        temp = list(map(int, input()))
        matrix.append(temp)
    start = []
    end = []
    for i in range(N):
        for j in range(N):
            # 도착점 end = [i, j]
            if matrix[i][j] == 3:
                end.append(i)
                end.append(j)
            # 시작점 start = [i, j]
            if matrix[i][j] == 2:
                start.append(i)
                start.append(j)
    print('#{} {}'.format(tc, map_around(matrix, start, end)))