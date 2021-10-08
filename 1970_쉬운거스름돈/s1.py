import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    print('#{}'.format(tc))
    money = int(input())
    if money >= 50000:
        i = 0
        while money >= 50000:
            money -= 50000
            i += 1
        print(i, end=' ')
    else:
        print(0, end=' ')

    if money >= 10000:
        i = 0
        while money >= 10000:
            money -= 10000
            i += 1
        print(i, end=' ')
    else:
        print(0, end=' ')

    if money >= 5000:
        i = 0
        while money >= 5000:
            money -= 5000
            i += 1
        print(i, end=' ')
    else:
        print(0, end=' ')

    if money >= 1000:
        i = 0
        while money >= 1000:
            money -= 1000
            i += 1
        print(i, end=' ')
    else:
        print(0, end=' ')

    if money >= 500:
        i = 0
        while money >= 500:
            money -= 500
            i += 1
        print(i, end=' ')
    else:
        print(0, end=' ')

    if money >= 100:
        i = 0
        while money >= 100:
            money -= 100
            i += 1
        print(i, end=' ')
    else:
        print(0, end=' ')

    if money >= 50:
        i = 0
        while money >= 50:
            money -= 50
            i += 1
        print(i, end=' ')
    else:
        print(0, end=' ')
    if money >= 10:
        i = 0
        while money >= 10:
            money -= 10
            i += 1
        print(i, end=' ')
    else:
        print(0, end=' ')
    print()