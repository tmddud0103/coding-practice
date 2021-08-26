# bfs
import sys
sys.stdin = open('input.txt')

def bfs(s, g):
    queue = [s]                                     # 시작점을 enqueue

    while len(queue):
        s = queue.pop(0)                            # 현재 위치를 dequeue

        if s == G:                                  # 현재 위치가 도착점이라면
            return dist[g]                          # 현재 위치의 거리를 반환

        for w in range(1, V+1):
            if edge[s][w] == 1 and dist[w] == 0:    # 연결되어 있으면서 아직 안 간 노드라면
                queue.append(w)                     # 다음 위치는 enqueue
                dist[w] = dist[s] + 1               # 다음 위치의 거리는 현재위치 + 1

    return 0                                        # 도착하지 못한 경우에는 0을 반환

T = int(input())

for test_case in range(1, T+1):
    V, E = list(map(int, input().split()))
    edge = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        edge[v1][v2] = 1
        edge[v2][v1] = 1
    S, G = list(map(int, input().split()))
    dist = [0 for _ in range(V + 1)]

    print('#{} {}'.format(test_case, bfs(S, G)))