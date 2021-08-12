import sys
sys.stdin = open('input.txt')

def bubble_sort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


test_case = int(input())

for tc in range(1, test_case + 1):
    count = int(input())
    number_list= list(map(int, input().split()))
    special_sort = [0] * count
    list_sort = bubble_sort(number_list)
    if count % 2 == 0: #짝수
        for i in range(0, count, 2): # 0 2 4 6 8
            special_sort[i + 1] = list_sort[i // 2]
            special_sort[count - i - 2] = list_sort[i // 2 + count // 2]
        print('#{}'.format(tc), end=' ')
        for i in range(10):
            if i > 10:
                break
            print(special_sort[i], end=' ')
        print()
    else: # 홀수
        for i in range(0, count - 1, 2):
            special_sort[i + 1] = list_sort[i//2]
            special_sort[count - i - 3] = list_sort[i // 2 + count // 2]
        special_sort[count - 1] = list_sort[count // 2]
        print('#{}'.format(tc), end=' ')
        for i in range(count):
            if i > 10:
                break
            print(special_sort[i], end=' ')
        print()


