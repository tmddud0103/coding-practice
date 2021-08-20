import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    total = 0
    day = list(map(int, input().split()))
    max_number = day[-1]
    for i in range(len(day) - 1, -1, -1):
        if day[i] > max_number:
            max_number = day[i]
        elif max_number > day[i]:
            total += (max_number - day[i])
    print(f'#{tc} {total}')
