import sys
sys.stdin = open('input.txt')

test_case = int(input())

def find_page(total_page, find_page):
    start = 1
    end = total_page
    count_a = 0
    center = 0
    while start <= end:
        center = (start + end) // 2
        count_a += 1
        if center == find_page:
            return count_a
        elif center < find_page:
            start = center
        elif center > find_page:
            end = center
    return count_a

for tc in range(1, test_case + 1):
    P, Pa, Pb = list(map(int, input().split()))
    finda = find_page(P, Pa)
    findb = find_page(P, Pb)
    if finda < findb:
        print('#{} A'.format(tc))
    elif finda > findb:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))
