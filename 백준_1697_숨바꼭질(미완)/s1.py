import sys
sys.stdin = open('input.txt')


TC = int(input())

for tc in range(1, TC + 1):

    N, K = list(map(int, input().split()))
    answer = 0
    if N == 0 and K !=0:
        N = 1
        answer += 1
    if N > K:
        answer += N - K
    elif N == K:
        pass
    else:
        i = 0
        while N*(2**i) > K or K > N*(2**(i+1)):
            i += 1

        j1 = K - N*(2**i)
        i1 = 2**i
        j2 = K - N*(2**(i+1))
        i2 = 2**(i+1)
        answer1 = 0
        answer2 = 0
        while i1 != 1 or j1 != 0:
            if i1 != 1 and j1 % 2 == 0:
                j1 = j1//2
                i1 = i1//2
                answer1 += 1
            elif j1 < 0:
                j1 += 1
                answer1 += 1
            elif j1 > 0:
                j1 -= 1
                answer1 += 1
            else:
                pass
        while i2 != 1 or j2 != 0:
            if i2 != 1 and j2 % 2 == 0:
                j2 = j2//2
                i2 = i2//2
                answer2 += 1
            elif j2 < 0:
                j2 += 1
                answer2 += 1
            elif j2 > 0:
                j2 -= 1
                answer2 += 1
            else:
                pass

        if answer1 > answer2:
            answer += answer2
        else:
            answer += answer1
    print(answer)
