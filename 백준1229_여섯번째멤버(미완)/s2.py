import sys
sys.stdin = open('input.txt')
N = int(input())

big_bang_number = [1]
add = 5


def bbnum(num, cnt, k):
    global big_bang_number, N, total
    # print(num,cnt,  'num')
    if cnt > 6:
        return
    if num==0:
        if cnt<total:
            total = cnt
        return
    for i in range(k, -1, -1):
        if i+5<k:
            return
        if num-big_bang_number[i]>=0:
            # print(big_bang_number[i])
            bbnum(num-big_bang_number[i], cnt+1, k)




while big_bang_number[-1] < N:
    next_number = big_bang_number[-1] + add
    big_bang_number.append(next_number)
    add += 4
big_bang_number.pop(-1)
total = 6
if N >=1791:
    print(4)
else:
    bbnum(N, 0, len(big_bang_number)-1)
    print(total)
