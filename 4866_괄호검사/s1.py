import sys
sys.stdin = open('input.txt')

def asdf():
    global sentence
    stack = []
    for i in sentence:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}':
            # '}'와 '{'을 짝지어주어야 하는데 스택의 길이가 0이라면 해보나마나
            # 바로 리턴 0
            #아래의 if문이 없으면 에러가 발생할 수 있음
            if len(stack) == 0:
                return 0
            if stack[-1] == '{':
                stack.pop()
            else:
                return 0
        elif i == ')':
            if len(stack) == 0:
                return 0
            if stack[-1] == '(':
                stack.pop()
            else:
                return 0
        else:
            pass
    # for문을 다 돌고 스택의 길이가 0이다
    # = {}, () 각각 짝을 찾아서 잘 없애줬다는 이야기
    # 1값을 리턴
    if len(stack) == 0:
        return 1
    # if문에 걸리지 않았다면 어떤 값이 남았다는 이야기
    # 0값을 리턴
    return 0

T = int(input())

for tc in range(1, T + 1):
    sentence = list(map(str, input()))
    print(f'#{tc} {asdf()}')


