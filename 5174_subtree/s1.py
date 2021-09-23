import sys
sys.stdin = open('input.txt')

def subtree(node):
    global t1, t2, n
    if node == 0:
        return 0
    n += 1
    subtree(t1[node])
    subtree(t2[node])
    return 0

TC = int(input())
for tc in range(1, TC+1):
    E, N = list(map(int, input().split()))
    node = list(map(int, input().split()))
    t1 = [0 for _ in range(E+2)]
    t2 = [0 for _ in range(E+2)]
    for i in range(0, E):
        if t1[node[i * 2]] == 0:
            t1[node[i * 2]] = node[i * 2 + 1]
        else:
            t2[node[i * 2]] = node[i * 2 + 1]
    n = 0
    subtree(N)
    print(f'#{tc} {n}')
