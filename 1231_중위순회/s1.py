import sys
sys.stdin = open('input.txt')

def check(n):
    global N, answer, total
    if n*2 <= N:
        check(n*2)
    answer += node[n]
    if n*2 + 1 <= N:
        check(n*2+1)
    return 0
# TC = int(input())
for tc in range(1, 11):
    N = int(input())
    left_node = [0 for _ in range(N+1)]
    right_node = [0 for _ in range(N+1)]
    node = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        if i < N//2:
            no, node[i], left_node[i], right_node[i] = list(map(str, input().split()))
        elif i == N//2 and N % 2 == 1:
            no, node[i], left_node[i], right_node[i] = list(map(str, input().split()))
        elif i == N//2 and N % 2 == 0:
            no, node[i], left_node[i] = list(map(str, input().split()))
        else:
            no, node[i] = list(map(str, input().split()))
    answer = ''
    check(1)
    print(f'#{tc} {answer}')