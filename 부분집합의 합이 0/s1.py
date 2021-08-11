import sys
sys.stdin = open('input.txt')
test_case = int(input())

for tc in range(1, test_case + 1):
# for tc in range(1, 2):
    list_of_numbers = list(map(int, input().split()))
    number_of_numbers = len(list_of_numbers)
    can_be_subset = 0
    for i in range(1 << number_of_numbers):
        sum_of_subset = 0
        subset = []
        for j in range(number_of_numbers + 1):
            if i & (1 << j):
                subset += [list_of_numbers[j]]
        for i in range(0, len(subset)):
            sum_of_subset += subset[i]
        if sum_of_subset == 0 and subset != []:
            can_be_subset += 1
    if can_be_subset > 0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))