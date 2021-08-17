import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
    dict = {}
    for i in range(0, len(str1)):
        dict[str1[i]] = 0
    for i in range(0, len(str2)):
        for key, value in dict.items():
            if str2[i] == key:
                dict[key] += 1
    print('#{} {}'.format(tc, max(dict.values())))



