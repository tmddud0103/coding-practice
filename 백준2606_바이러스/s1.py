import sys
sys.stdin = open('input.txt')

com = int(sys.stdin.readline().rstrip())
net = int(sys.stdin.readline().rstrip())
mat = [[0 for _ in range(1 + com)] for i in range(1+com)]
checked = [0] * (com+1)
checked[1] = 1
stack = [1]
cnt = 0
for _ in range(net):
    a, b = list(map(int, sys.stdin.readline().split()))
    mat[a][b], mat[b][a] = 1, 1
while stack:
    k = stack.pop(0)
    for i in range(1, com+1):
        if mat[k][i] == 1 and checked[i] == 0:
            checked[i] = 1
            stack.append(i)
print(sum(checked)-1)
