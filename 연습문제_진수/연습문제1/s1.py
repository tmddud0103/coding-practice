import sys
sys.stdin = open('input.txt')

N = list(map(int, input()))
print(len(N))
print(N)
answer = []
for i in range(len(N)//7):
    temp = N[0+i*7 : 7+i*7]
    k = 0
    temp2 = 0
    for j in range(6, -1, -1):
        temp2 += temp[j]*(2**k)
        k += 1
    answer.append(temp2)
print(answer)