import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))
    n_list = list(map(int, input().split()))
    for i in range(M):
        a = n_list.pop(0)
        n_list.append(a)
    print('#{} {}'.format(tc, n_list[0]))



# import sys; sys.stdin = open("input.txt")
# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     queue = list(map(int, input().split()))
#     print("#{} {}".format(tc, queue[M % N]))