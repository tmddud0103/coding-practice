import sys
X = int(sys.stdin.readline().rstrip())
cnt = 0
while X != 1:
    if X % 3 == 0:
        X = X // 3
        cnt += 1

    elif X % 2 == 0:
        if (X-1) % 9 == 0:
            X -= 1
            cnt += 1
        else:
            X = X // 2
            cnt += 1

    # elif X > 20:
    #     while X % 3 != 0:
    #         print('x', X, cnt)
    #         X -= 1
    #         cnt += 1

    else:
        X -= 1
        cnt += 1
        if X != 1 and (X-1) % 9 == 0:
            X -= 1
            cnt += 1

    print(X, cnt)
print(cnt)