import sys
sys.stdin = open('input.txt')

big_bang_number = [1]
add = 5
pre_bb2 = []

def pre_bb(N):
    global big_bang_number, pre_bb2
    for i in range(len(big_bang_number)):
        if big_bang_number[i] <= N and N < big_bang_number[i + 1]:
            pre_bb2 = big_bang_number[0:i+1]
            return 0

while big_bang_number[-1] < 1000000:
    next_number = big_bang_number[-1] + add
    big_bang_number.append(next_number)
    add += 4

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    add = 5
    num = 0
    min_num = 0
    N1 = N
    pre_bb(N)
    pre_bb1 = pre_bb2[:]
    print(pre_bb1)
    while N != 0:
        if pre_bb2[-1] <= N:
            N -= pre_bb2[-1]
            num += 1
        else:
            pre_bb2.pop()


    if num > 6:
        pre_bb1.pop()
        while N1 != 0:
            if pre_bb1[-1] <= N1:
                N1 -= pre_bb1[-1]
                min_num += 1
            else:
                pre_bb1.pop()

    if N1 == 0 and min_num <= num:
        print(min_num)
    else:
        print(num)