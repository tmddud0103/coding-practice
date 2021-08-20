import sys
sys.stdin = open('input.txt')

# T = int(input())
for tc in range(1, 11):
    T, line = list(map(int, input().split()))
    line_list = list(map(int, input().split()))
    length = len(line_list)
    graph = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0 for _ in range(100)]

    for i in range(line):
        go = line_list[2 * i]
        end = line_list[2 * i + 1]
        graph[go][end] = 1

    def dfs(v):
        global graph, visited, line
        stack = [v]

        while len(stack):
            v = stack.pop()
            if visited[v] == 0:
                visited[v] = 1
                # print(f'방문한 위치 {v} visited {visited}')
                if v == 99:
                    return 1
            for w in range(1, 100):
                if graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)
        return 0
    print(f'#{T} {dfs(0)}')