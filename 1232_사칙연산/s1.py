import sys
sys.stdin = open('input.txt')

def trees(n):
    global tree, sub_tree
    n = int(n)
    if tree[n] == '-':
        left = int(trees(sub_tree[n][0]))
        right = int(trees(sub_tree[n][1]))
        return (int(left)-int(right))
    elif tree[n] == '+':
        left = int(trees(sub_tree[n][0]))
        right = int(trees(sub_tree[n][1]))
        return (int(left) + int(right))
    elif tree[n] == '*':
        left = int(trees(sub_tree[n][0]))
        right = int(trees(sub_tree[n][1]))
        return (int(left) * int(right))
    elif tree[n] == '/':
        left = int(trees(sub_tree[n][0]))
        right = int(trees(sub_tree[n][1]))
        return (int(left) // int(right))

    else:
        return tree[n]



for tc in range(1, 11):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    sub_tree = [0]
    for i in range(1, N + 1):
        temp = list(map(str, input().split()))
        tree[i] = temp[1]
        try:
            sub_tree.append(temp[2:])
        except:
            pass
    print(f'#{tc} {trees(1)}')