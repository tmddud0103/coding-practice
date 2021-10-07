import sys
sys.stdin = open('sample_input.txt')

def quickSort(p, s, e, nlist):
    ee = e
    if s > e:
        return nlist
    if s == e:
        if nlist[s] < nlist[p]:
            nlist[s], nlist[p] = nlist[p], nlist[s]
    while s < e:
        if nlist[s] <= nlist[p] and nlist[p] <= nlist[e]:
            s += 1
            e -= 1
        elif nlist[s] >= nlist[p] and nlist[p] >= nlist[e]:
            nlist[s], nlist[e] = nlist[e], nlist[s]
            s += 1
            e -= 1
        elif nlist[s] <= nlist[p]:
            s += 1
        else:
            e -= 1
    if nlist[s] > nlist[p]:
        s -= 1
        nlist[s], nlist[p] = nlist[p], nlist[s]
    else:
        nlist[s], nlist[p] = nlist[p], nlist[s]

    print(nlist, p, s, e)
    nlist = quickSort(p, p+1, s-1, nlist)
    nlist = quickSort(s+1, s+2, ee, nlist)
    print(nlist)
    return nlist


TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    nlist = list(map(int, input().split()))
    quickSort(0, 1, N-1, nlist)
    print(nlist)
    # for i in range(0, N-1):
    #     if nlist[i] > nlist[i+1]:
    #         quickSort(0, 1, N - 1, nlist)
    print('#{} {}'.format(tc, nlist[N//2]))