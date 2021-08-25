import sys
sys.stdin = open('input.txt')

# V => 노드, 정점
# E => 엣지, 간선

V, E = list(map(int, input().split()))

graph_list = list(map(int, input().split()))

graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]

visited = [0 for _ in range(V + 1)]

for i in range(E):
    start = graph_list[i * 2]
    end = graph_list[i * 2 + 1]
    graph[start][end] = 1
    graph[end][start] = 1

def bfs(v):
    # v = 시작하는 노드
    queue = [v]

    while len(queue):           # queue의 값이 비어있을 때까지
        v = queue.pop(0)        # 첫번째 = 맨 앞의 값을 가져와야한다
        if not visited[v]:          # 방문하지 않았다면
            visited[v] = 1
            print('{}을 방문했습니다. {}'.format(v, visited))

            for w in range(1, V + 1):
                if graph[v][w] and visited[w] == 0:
                    queue.append(w)


bfs(1)