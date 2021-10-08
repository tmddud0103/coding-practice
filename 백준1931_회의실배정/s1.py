import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().lstrip())
nlist = []
for _ in range(n):
    nlist.append(list(map(int, sys.stdin.readline().split())))
nlist.sort()
nlist.sort(key=lambda x:x[1])
cnt = 0
close = -1
for time in nlist:
    if close<=time[0]:
        close = time[1]
        cnt+=1
print(cnt)