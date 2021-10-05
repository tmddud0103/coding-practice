import sys
sys.stdin = open('input.txt')
TC = int(sys.stdin.readline().rstrip())

def cnt(N, count):
    global min_cnt
    if count > 4:
        return 0

    for i in range(int(N ** 0.5), int((N//(4-count)) ** 0.5), -1):
        if i > 0:
            if N == i*i:
                min_cnt = min(min_cnt, count+1)
                return
            cnt(N-i*i, count+1)


for tc in range(1, TC + 1):
    N = int(sys.stdin.readline().rstrip())
    min_cnt = 4
    cnt(N, 0)
    print(min_cnt)