import sys
sys.stdin = open('input.txt')

def pre_order(n):
    if n:
        print(n)
        pre_order(left[n])
        pre_order(right[n])

def in_order(n):
    if n:
        in_order(left[n])
        print(n)
        in_order(right[n])

def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n)

V = int(input())
edge = list(map(int, input().split()))
E = V - 1                   # V개의 정점이 있는 트리의 간선 수
left = [0] * (V + 1)        # 부모를 인덱스로 자식번호 저장
right = [0] * (V + 1)
# for i in range(0, len(edge)//2):
#     if left[edge[i * 2]] == 0:
#         left[edge[i * 2]] = edge[i * 2+ 1]
#     else:
#         right[edge[i * 2]] = edge[i * 2+ 1]
for i in range(E):
    p, c = edge[i * 2], edge[i * 2 + 1]
    if left[p] == 0:    # p의 왼쪽 자식이 없으면
        left[p] = c
    else:               # 왼쪽 자식이 있으면 오른쪽 자식으로 저장
        right[p] = c
print('pre')
pre_order(1)
print('in')
in_order(1)
print('post')
post_order(1)
