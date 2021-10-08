import sys
sys.stdin = open('sample_input.txt')

def min_factory(i, temp):
    global min_price, check, N, mat
    if temp > min_price:
        return
    if i == N:
        if temp < min_price:
            min_price = temp
        return
    for j in range(N):
        if check[j] == 0:
            check[j] = 1
            min_factory(i+1, temp + mat[i][j])
            check[j] = 0

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    min_price = 100*N
    check = [0]*N
    min_factory(0, 0)
    print('#{} {}'.format(tc, min_price))