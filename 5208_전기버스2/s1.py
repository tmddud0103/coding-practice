import sys
sys.stdin = open('sample_input.txt')

def charge(ch, station):
    global nlist, N, total
    if station >= N-1 or nlist[station] + station > N-1:
        if ch < total:
            total = ch
        return
    if ch >= total:
        return
    for i in range(1, nlist[station] + 1):
        if station + i <= N-1:
            charge(ch+1, station + i)


TC = int(input())

for tc in range(1,TC+1):
    nlist = list(map(int, input().split()))
    N = nlist[0]
    total = N
    charge(0, 1)
    print('#{} {}'.format(tc, total))