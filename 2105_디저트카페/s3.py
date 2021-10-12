# 남의 풀이 내 것과 얼마나 다른지 궁금해서 가져옴

import sys
sys.stdin = open('sample_input.txt')
D = ((1, 1), (1, -1), (-1, -1), (-1, 1))


def dfs(cnt, r, c, sr, sc, d):
    global answer

    if d == 4:
        return

    if (r, c) == (sr, sc):
        answer = max(answer, cnt)
        return

    if 0 <= r < n and 0 <= c < n and not visit[arr[r][c]]:
        visit[arr[r][c]] = 1
        dfs(cnt + 1, r + D[d][0], c + D[d][1], sr, sc, d)
        dfs(cnt + 1, r + D[(d + 1) % 4][0], c + D[(d + 1) % 4][1], sr, sc, d + 1)
        visit[arr[r][c]] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * 101
    answer = -1
    for i in range(n - 2):
        for j in range(1, n - 1):
            visit[arr[i][j]] = 1
            dfs(1, i + 1, j + 1, i, j, 0)
            visit[arr[i][j]] = 0

    print(f"#{tc} {answer}")