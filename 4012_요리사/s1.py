import sys
from itertools import combinations
sys.stdin = open('sample_input.txt')

def cook(a, b):
    global mat, n, total
    temp = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            temp = temp + mat[a[i]][a[j]] + mat[a[j]][a[i]] - mat[b[i]][b[j]] - mat[b[j]][b[i]]
    temp = abs(temp)
    if total > temp:
        total = temp

TC = int(input())

for tc in range(1, TC + 1):
    n = int(input())
    com = []
    a = []
    mat = []
    for i in range(n):
        a.append(i)
        mat.append(list(map(int, input().split())))
    for i in combinations(a, len(a)//2):
        com.append(i)
    # print(com)
    total = 20000
    for j in range(len(com)//2):
        cook(com[j], com[-j-1])
    print('#{} {}'.format(tc, total))