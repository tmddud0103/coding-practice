import sys
sys.stdin = open('input.txt')
remo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def problem(now, end):
    global ans
    if now == end:
        temp = int(''.join(map(str, d)))
        ans = min(ans, abs(intn-temp)+end)
        return
    for i in range(0, 10):
        if remo[i]==1:
            d.append(i)
            problem(now+1, end)
            d.pop()


n = str(sys.stdin.readline().rstrip())
intn = int(n)
lenn = len(n)
countbrokennumber = int(sys.stdin.readline().lstrip())
brokennum = list(map(int, sys.stdin.readline().split()))
for i in range(countbrokennumber):
    remo[brokennum[i]] = 0
ans = abs(intn-100)
if countbrokennumber == 0:
    print(min(lenn, ans))
elif countbrokennumber == 10:
    print(ans)
else:
    d = []
    if lenn == 1:
        for i in range(1, 3):
            problem(0, i)
        print(ans)
    else:
        for i in range(lenn - 1, lenn+2):
            problem(0, i)
        print(ans)
