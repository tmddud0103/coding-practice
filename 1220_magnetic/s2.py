# 교수님 풀이
import sys
sys.stdin = open('input.txt')

# 10th
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 열 우선 순회
    for c in range(N):
        # 상태값, 0 = 1을 만나기전 상태, 1 = 1을 만난 상태
        state = 0
        for r in range(N):
            if state == 0 and arr[r][c] == 1:
                state = 1
            elif state == 1 and arr[r][c] == 2:
                ans += 1
                state = 0
    print(ans)
