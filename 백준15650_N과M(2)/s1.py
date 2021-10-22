import sys
sys.stdin = open('input.txt')
n, m = list(map(int, sys.stdin.readline().split()))
arr = []
used = [0]*n
total = []
def perm(inputlist, ran, j):
    if m == ran:
        total.append(inputlist[:])
        return
    for i in range(j, n):
        if used[i]==0:
            used[i]=1
            inputlist.append(arr[i])
            perm(inputlist, ran+1, i)
            inputlist.pop()
            used[i] = 0


for i in range(1, n+1):
    arr.append(i)
perm([], 0, 0)
for i in range(len(total)):
    for j in range(m):
        print(total[i][j], end=' ')
    print()
