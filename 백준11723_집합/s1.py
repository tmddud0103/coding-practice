import sys
sys.stdin = open('input.txt')

import sys

TC = int(sys.stdin.readline())
S = set()
for tc in range(1, TC + 1):
    N = sys.stdin.readline().rstrip()

    if 'empty' in N or 'all' in N:
        N = N
    else:
        N, M = N.split()

    if N == 'add':
        S.add(M)
    elif N == 'remove':
        S.discard(M)
    elif N == 'check':
        if M in S:
            print('1')
        else:
            print('0')
    elif N == 'toggle':
        if M in S:
            S.discard(M)
        else:
            S.add(M)
    elif N == 'all':
        S = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif N == 'empty':
        S.clear()
    else:
        pass