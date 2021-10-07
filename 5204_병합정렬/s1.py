import sys
sys.stdin = open('sample_input.txt')

def mergeSort(N, nlist):
    if N == 1: return nlist
    # elif N == 3:
    #     mid = (N+1)//2
    else:
        mid = N // 2
    left = nlist[:mid]
    right = nlist[mid:]
    left = mergeSort(N//2, left)
    right = mergeSort(N - N//2, right)

    return merge(left, right)

def merge(left, right):
    global cnt
    i, j = 0, 0
    ll, lr = len(left), len(right)
    result = []
    while ll > i or lr > j:
        if ll > i and lr > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif ll == i+1 and lr == j:
            result.append(left[i])
            i += 1
            cnt += 1
        elif lr - j > 0:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    return result



TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    nlist = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, mergeSort(N, nlist)[N//2], cnt))

