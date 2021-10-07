import sys
sys.stdin = open('sample_input.txt')

def binarySearch(i, s, e, nlist):
    global cnt, check
    while s <= e:
        mid = (e+s)//2
        if nlist[mid] == i:
            cnt += 1
            return
        elif nlist[mid] > i:
            if check == 2: return
            check = 2
            e = mid -1
        else:
            if check == 1: return
            check = 1
            s = mid + 1
    return



TC = int(input())

for tc in range(1,TC+1):
    n, m = list(map(int, input().split()))
    nlist = sorted(list(map(int, input().split())))
    mlist = list(map(int, input().split()))
    cnt = 0

    for i in mlist:
        check = 0
        binarySearch(i, 0, n-1, nlist)
    print('#{} {}'.format(tc, cnt))