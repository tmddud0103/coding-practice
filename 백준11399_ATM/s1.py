import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
time_list = [0]*N
time_list[0] = nlist[0]
for i in range(1, N):
    time_list[i] = time_list[i-1] + nlist[i]
print(sum(time_list))

