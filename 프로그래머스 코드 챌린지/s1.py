import sys
sys.stdin = open('input.txt')


def solution(a, s):
    answer = []
    for i in s:
        temp = a[:i]
        del a[:i]
        stack = [temp]
        count = 0
        while count != len(stack):
            so = stack[count]
            for k in range(len(so)-1, 0, -1):
                if so[k] == so[k - 1]:
                    so_fake = so[:]
                    ta = so_fake.pop(k)
                    te = so_fake.pop(k-1)
                    so_fake.insert(k-1, te * 2)
                    if so_fake in stack:
                        break
                    stack.append(so_fake[:])
            count += 1
        print(stack)
        answer.append(len(stack))
    return answer



a = list(map(int, input().split()))
s = list(map(int, input().split()))
print(solution(a, s))