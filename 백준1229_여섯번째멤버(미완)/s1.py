N = int(input())

big_bang_number = [1]
add = 5
num = 0
while big_bang_number[-1] < 1000000:
    next_number = big_bang_number[-1] + add
    big_bang_number.append(next_number)
    add += 4


while N != 0:
    for i in range(len(big_bang_number)):
        if big_bang_number[i] <= N and N < big_bang_number[i + 1]:
            pre_bb = big_bang_number[0:i]
            print(pre_bb)
            break
    N -= big_bang_number[i]
    num += 1
print(num)