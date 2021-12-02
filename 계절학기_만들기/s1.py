import sys
sys.stdin = open('input.txt')

nlist = [0]*101
mat = [[0]*101 for _ in range(101)]
nlist[1] = 1
for i in range(1, 7):
    mat[1][i] = 1
for i in range(2, 100):
    for j in range(1, 101):
        for k in range(1, 7):
            if j+k <= 100:
                mat[i][j+k] += mat[i-1][j]
TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    ans = 0
    for i in range(1, 101):
        ans += mat[i][n]**2
    print('#{} {}'.format(tc,ans%10000000))






# for i in range(2, 7):
#     nlist[i] = 1+sum(nlist)
# for i in range(7, 101):
#     temp = 0
#     for j in range(i-1, i-7, -1):
#         temp += nlist[j]
#     nlist[i] = temp
# print(nlist)
# n = int(input())
# print(nlist[n]**2)