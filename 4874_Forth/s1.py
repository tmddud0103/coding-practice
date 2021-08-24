import sys
sys.stdin = open('input.txt')

def forth():
    for i in range(len(calculation)):
        # 숫자일 경우 => try를 통해 int로 바꿀 수 있을 것이다.
        try:
            c = int(calculation[i])
            stack.append(str(c))
        # int로 바꾸는데 에러가 뜬다 = 숫자가 아니다
        # 사칙연산 + '.' 중에 하나가 나올 것이다
        except:
            # 마무리 마침표
            # 스택 안에있는 숫자가 2개 이상이면 마지막 값만 리턴하면 될 줄 알았는데 답이 틀림
            # 마침표를 만났는데 스택 안에 숫자값이 2개 이상이라면 error 리턴
            if calculation[i] == '.':
                if len(stack) >= 2:
                    return 'error'
                return stack[-1]
            if len(stack) >= 2:
                if calculation[i] == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a) + int(b))
                if calculation[i] == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a) * int(b))
                if calculation[i] == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b) // int(a))
                if calculation[i] == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b) - int(a))
            # 사칙연산을 만났는데, 스택 안에 저장된 숫자가 2개 이하라면?
            # 계산 못함
            # 에러 리턴
            else:
                return 'error'

TC = int(input())
for tc in range(1, TC + 1):
    stack = []
    calculation = list(map(str, input().split()))
    print('#{} {}'.format(tc, forth()))
