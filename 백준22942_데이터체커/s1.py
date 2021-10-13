import sys
sys.stdin = open('input.txt')

def circle(p, r):
    for j in range(p - r+1, p + r):
        st[j] += 1
    if st[p-r] != st[p+r]:
        return 'No'
    return 'Yes'

n = int(sys.stdin.readline().lstrip())

st = [0]*2000001
for i in range(n):
    p, r = list(map(int, sys.stdin.readline().split()))
    p += 1000000
    answer = circle(p, r)
    if answer == 'No':
        print('NO')
        break
if answer == 'Yes':
    print('YES')

