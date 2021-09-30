N = list(map(str, input()))
cnt = 0
for i in range(len(N)):
    if N[i] == ' ':
        if i != 0 and i != len(N)-1:
            cnt += 1
if N == [' ']:
    print(0)
else:
    print(cnt+1)
    print('a')