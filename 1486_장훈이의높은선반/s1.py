import sys
sys.stdin = open('input.txt')

def tower(now, temp):
    global n, b, people_list, min_but_over_b
    if temp >= b and temp < min_but_over_b:
        min_but_over_b = temp
    if min_but_over_b <= temp:
        return
    for j in range(now+1, n):
        tower(j, temp + people_list[j])


TC = int(input())

for tc in range(1, TC + 1):
    n, b = list(map(int, input().split()))
    people_list = list(map(int, input().split()))
    total = sum(people_list)
    min_but_over_b = total
    for i in range(n):
        temp = people_list[i]
        tower(i, temp)
    print('#{} {}'.format(tc, min_but_over_b-b))