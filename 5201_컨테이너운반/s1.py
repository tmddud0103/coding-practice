import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))
    nlist = sorted(list(map(int, input().split())), reverse=True)
    mlist = sorted(list(map(int, input().split())), reverse=True)
    i = 0
    total = 0
    for m in mlist:
        for n in range(i, len(nlist)):
            if m >= nlist[n]:
                total += nlist[n]
                i = n+1
                break
    print('#{} {}'.format(tc, total))