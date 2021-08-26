import sys
sys.stdin = open('input.txt')

def check_node(start):
    global stack, min_stack, checked_list
    # 현재 미니멈스택보다 쌓여있는 스택이 많으면 더 볼 이유가 없다
    # 바로 리턴
    if min_stack <= stack:
        return
    # 스타트와 앤드 값이 같으면 스택을 비교한다
    if start == end:
        if min_stack > stack:
            min_stack = stack
            return
        else:
            return
    # 스타트를 1로만들어서 이미 지나갔다는 체크
    checked_list[start] = 1
    for i in range(1, V+1):
        # 현재 위치에서 길이 존재하는데, 이전에 지나간 노드가 아닌 경우
        if matrix[start][i] == 1 and checked_list[i] == 0:
            checked_list[i] = 1                 # 지나갈 길이라고 체크
            stack += 1
            check_node(i)
            stack -= 1
            checked_list[i] = 0

TC = int(input())
for tc in range(1, TC + 1):
    V, E = list(map(int, input().split()))
    matrix = [[0 for _ in range(0, V+1)] for _ in range(V+1)]
    for _ in range(E):
        x1, x2 = list(map(int, input().split()))
        matrix[x1][x2], matrix[x2][x1] = 1, 1

    start, end = list(map(int, input().split()))
    checked_list = [0] * (V + 1)
    checked_list[0] = 1
    stack = 0
    # 최대는 노드의 길이 + 1 만큼
    min_stack = V + 2
    check_node(start)
    if min_stack == V +2:
        min_stack = 0
    print('#{} {}'.format(tc, min_stack))