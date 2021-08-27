import sys
sys.stdin = open('input.txt')

TC = int(input())

def degree90():
    global c1, c2, h1, h2, house_list
    c1, c2 = c2, 100 - c1
    h1, h2 = h2, 100 - h1
    for i in range(len(house_list)//2):
        house_list[i*2], house_list[i*2 + 1] = house_list[i*2 + 1], 100 - house_list[i*2 + 1]


def right():
    global house_list
    out_a = []
    out_b = []
    inside = []
    total = 0
    if c1-h1 > 0:
        a1, a2 = h1, h2
        b1, b2 = c1, c2

        rm = abs(b2 - a2) / (abs(b1 - a1) + abs(b2 - a2))
        cm = abs(a1 - a1) / (abs(b1 - a1) + abs(b2 - a2))
        for i in range(N):
            r, c = house_list.pop(0), house_list.pop(0)
            if rm * r + cm * c < rm * a1 + cm * a2:
                out_a.append([rm * r + cm * c, r, c])
            elif rm * r + cm * c > rm * b1 + cm * b2:
                out_b.append([rm * r + cm * c, r, c])
            else:
                inside.append([rm * r + cm * c, r, c])
        inside.sort()
        out_a.sort()
        out_b.sort()
        print(out_a)
        print(out_b)
        while out_a:
            temp, x1, x2 = out_a.pop(0)
            total += abs(a1 - x1) + abs(a2 - x2)
            print(total)
            a1, a2 = x1, x2
        while out_b:
            temp, x1, x2 = out_b.pop(0)
            total += abs(b1 - x1) + abs(b2 - x2)
            b1, b2 = x1, x2
        inside.append([0, b1, b2])
        while inside:
            temp, x1, x2 = inside.pop(0)
            total += abs(a1 - x1) + abs(a2 - x2)
            a1, a2 = x1, x2
    else:
        a1, a2 = h1, h2
        b1, b2 = c1, c2

        rm = abs(b2 - a2) / (abs(b1 - a1) + abs(b2 - a2))
        cm = abs(a1 - a1) / (abs(b1 - a1) + abs(b2 - a2))
        for i in range(N):
            r, c = house_list.pop(0), house_list.pop(0)
            if rm * r + cm * c < rm * a1 + cm * a2:
                out_a.append([rm * r + cm * c, r, c])
            elif rm * r + cm * c > rm * b1 + cm * b2:
                out_b.append([rm * r + cm * c, r, c])
            else:
                inside.append([rm * r + cm * c, r, c])
        inside.sort(reverse=True)
        out_a.sort(reverse=True)
        out_b.sort(reverse=True)
        print(out_a)
        print(out_b)
        while out_a:
            temp, x1, x2 = out_a.pop(0)
            total += abs(a1 - x1) + abs(a2 - x2)
            print(total)
            a1, a2 = x1, x2
        while out_b:
            temp, x1, x2 = out_b.pop(0)
            total += abs(b1 - x1) + abs(b2 - x2)
            b1, b2 = x1, x2
        inside.append([0, b1, b2])
        while inside:
            temp, x1, x2 = inside.pop(0)
            total += abs(a1 - x1) + abs(a2 - x2)
            a1, a2 = x1, x2
    return total




for tc in range(1, 4):
    N = int(input())
    house_list = list(map(int, input().split()))
    c1, c2 = house_list.pop(0), house_list.pop(0)
    h1, h2 = house_list.pop(0), house_list.pop(0)
    if (c1-h1 > 0 and c2-h2 > 0) or (c1-h1 < 0 and c2-h2 < 0):
        print(right())
    else:
        degree90()
        print(right())