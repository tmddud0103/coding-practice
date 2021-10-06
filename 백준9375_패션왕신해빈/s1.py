import sys
sys.stdin = open('input.txt')


TC = int(sys.stdin.readline().rstrip())
for _ in range(TC):
    N = int(sys.stdin.readline().rstrip())
    clothType = {}
    for _ in range(N):
        clothes, type = sys.stdin.readline().split()
        if type in clothType:
            clothType[type] += 1
        else:
            clothType[type] = 1
    answer = 1
    for value in clothType.values():
        answer = answer * (value + 1)
    print(answer - 1)