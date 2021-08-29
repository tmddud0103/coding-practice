import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    memory = list(map(int, input()))
    length = len(memory)
    reset = [0 for _ in range(length)]

    count = 0
    while memory != reset:
        for i in range(length):
            if memory[i] != reset[i]:
                count += 1
                for j in range(0, length-i):
                    reset[i+j] = memory[i]
    print('#{} {}'.format(tc, count))