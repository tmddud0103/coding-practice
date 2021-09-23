import sys
sys.stdin = open('input.txt')



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    hip_tree = list(map(int, input().split()))
    tree = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        if i == 1:
            tree[i] = hip_tree[i-1]
        else:
            tree[i] = hip_tree[i-1]
            if tree[i//2] > tree[i]:
                k=i
                while k!=1 and tree[k//2] > tree[k]:
                    tree[k // 2], tree[k] = tree[k], tree[k // 2]
                    k = k//2
    num_last_node = len(tree) - 1
    total = 0
    while num_last_node != 1:
        num_last_node = num_last_node//2
        total += tree[num_last_node]
    print(f'#{tc} {total}')