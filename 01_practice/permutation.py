# 순열의 개념
def permutation(k):
    global visited
    if k == N:
        # total.append(visited)
        print(visited)

    for idx in range(k, N):
        visited[k], visited[idx] = visited[idx], visited[k]
        permutation(k + 1)
        visited[k], visited[idx] = visited[idx], visited[k]

N = 5
visited = [0] * N       # [0, 1, 2]

for i in range(N):
    visited[i] = i

permutation(0)