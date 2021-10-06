import sys
import math
sys.stdin = open('input.txt')




TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    total = []
    answer = 0
    N = int(sys.stdin.readline().rstrip())
    total.append([N, 0, 0])
    i = 0

    while N - (3*i) >= 0:
        j = 0
        while N - (2*j) - (3*i) >= 0:
            n = N - (2*j) - (3*i)
            total.append([n, j, i])
            j += 1
        i += 1
    for to in total:
        to123 = to[0] + to[1] + to[2]
        answer += (math.factorial(to123))//(math.factorial(to[0]) * math.factorial(to[1]) * math.factorial(to[2]))
    print(answer-1)