import sys
sys.stdin = open('input.txt')

def dfs(v):
    global graph, visited, V, end
    stack = [v]
    while len(stack):
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            # print(f'방문한위치 {v} visited{visited}')

            # 현재위치 v가 우리가 원하는 end값이라면
            # start에서 end까지 갈 수 있다는 뜻
            # 1값 리턴
            if v == end:
                return 1
            for w in range(1, V+1):
                if graph[v][w] == 1 and visited[w] == 0:
                    stack.append(w)
    # 위의 if문에 걸리지 않았다면 = start로 시작해서 end까지 갈 수 없다는 뜻
    # 0값 리턴
    return 0


T = int(input())

for tc in range(1, T + 1):
    # V => 노드
    # E => 간선
    V, E = list(map(int, input().split()))
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V + 1)]

    for i in range(E):
        x, y = list(map(int, input().split()))
        graph[x][y] = 1
    start, end = list(map(int, input().split()))
    print(f'#{tc} {dfs(start)}')
