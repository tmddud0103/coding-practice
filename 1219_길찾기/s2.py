# 참고 하나도 없이 혼자서 s1과 같은 코드 만들기
import sys
sys.stdin = open('input.txt')

def dfs():
    global visited, matrix, line
    end = 99
    start = 0
    stack = [start]

    while len(stack):
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = 1
            if now == 99:
                return 1
        for j in range(100):
            if matrix[now][j] == 1 and visited[j] == 0:
                stack.append(j)
    return 0


for tc in range(10):
    T, line = list(map(int, input().split()))
    path = list(map(int, input().split()))
    matrix = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0 for _ in range(100)]
    for i in range(line):
        go = path[2 * i]
        to = path[2 * i + 1]
        matrix[go][to] = 1
    print(dfs())
