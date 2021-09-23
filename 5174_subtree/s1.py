import sys
sys.stdin = open('input.txt')

def subtree(node):
    global root, t1, t2, n
    if node == 0:
        return n
    n += 1
    subtree(t1[node])
    subtree(t2[node])
    return n


TC = int(input())
for tc in range(1, TC+1):
    E, N = list(map(int, input().split()))
    tree = list(map(int, input().split()))
    t1 = [0 for _ in range(E+2)]
    t2 = [0 for _ in range(E+2)]
    find_node_tree = [0 for _ in range(E+2)]
    for i in range(0, E):
        if t1[tree[i * 2]] == 0:
            t1[tree[i * 2]] = tree[i * 2 + 1]
            find_node_tree[tree[i * 2 + 1]] += 1
        else:
            t2[tree[i * 2]] = tree[i * 2 + 1]
            find_node_tree[tree[i * 2 + 1]] += 1
    for j in range(1, E+2):
        if find_node_tree[j] == 0:
            root = j
    n = 0
    a = subtree(N)
    print(f'#{tc} {a}')
