import sys
sys.stdin = open('sample_input.txt')

def sese(start, temp):
    global N, se, total
    e = se[start][1]
    for j in range(start, N):
        if e <= se[j][0]:
            sese(j, temp + 1)
    if temp > total:
        total = temp


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    se = sorted([list(map(int, input().split())) for _ in range(N)])
    total = 0
    for i in range(N):
        sese(i, 1)
    print('#{} {}'.format(tc, total))
