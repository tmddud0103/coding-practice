import sys
sys.stdin = open('input.txt')

T = int(input())

def asdf():
    global sentence
    stack = []
    for i in sentence:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    return(len(stack))

for tc in range(1, T + 1):
    sentence = list(map(str, input()))
    print(f'#{tc} {asdf()}')