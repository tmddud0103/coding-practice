import sys
sys.stdin = open('input.txt')

# 후위 계산식 만들기
# 후위 표기식 진짜 어렵다
# +, * 두개 밖에 없는데도 이렇게 까다로운데
# 사칙연산에 괄호 있으면 어캐푸누...?
# 말하자마자 나오네 선넘네
def postfix(asd):
    # 완성된 후위 계산식은 total에 저장
    total = ''
    # 사직연산 (여기선 더하기와 곱하기) 그리고 열린괄호를 저장
    temp = []
    for i in range(0, length):
        # 계산기2에서 긁어온 try
        try:
            a = int(asd[i])
            total += str(a)
        except:
                # 저장된 사칙연산이 없다면 바로 저장
            if len(temp) == 0:
                temp.append(asd[i])
                # 적어도 1개 이상 temp에 저장이 되어있다
            else:
                # 저장된 사칙연산 +
                # 저장할 사칙연산 *
                # 그냥 저장하면 된다
                if temp[-1] == '+' and asd[i] == '*':
                    temp.append(asd[i])
                # 저장된 사칙연산 +
                # 저장할 사칙연산 +
                # 저장할 사칙연산을 바로 토탈에 저장해도 된다
                elif temp[-1] == '+' and asd[i] == '+':
                    total += asd[i]
                # 저장된 사칙연산 *
                # 저장할 사칙연산 *
                # 그냥 저장하면 된다
                elif temp[-1] == '*' and asd[i] == '*':
                    total += asd[i]
                # 저장된 사칙연산 *
                # 저장할 사칙연산 +
                # 여기가 머리 아픈 포인트
                elif temp[-1] == '*' and asd[i] == '+':
                # + * 가 저장되어있는 경우 => 둘 다 total을 저장하고 +를 저장한다
                    if len(temp) == 2 and temp[-2] =='+':
                        temp.pop()
                        total += '*'
                        temp.pop()
                        total += '+'
                        temp.append(asd[i])
                # 그 외 => *을 토탈에, +를 temp에
                    else:
                        temp.pop()
                        total += '*'
                        temp.append(asd[i])
                # 닫힌 괄호 => 어딘가에 열린괄호가 나온다
                # 나올때까지 pop
                elif asd[i] == ')':
                    while temp[-1] != '(':
                        total += temp.pop()
                    temp.pop()
                elif asd[i] == '(' or temp[-1] =='(':
                    temp.append(asd[i])
                else:
                    pass
                # print(not_num)
    while len(temp) != 0:
        a = temp.pop()
        total += a
    return total

# 후위 표기식 정의하다가 후위표기식을 계산식을 정의하니 이렇게 쉽네
# 세상에
def calculate_postfix(lists):
    cal = []
    for i in range(0, len(postfix(calculate))):
        try:
            a = int(lists[i])
            cal.append(a)
        except:
            if lists[i] == '+':
                b = cal.pop()
                c = cal.pop()
                cal.append(b + c)
            else:
                b = cal.pop()
                c = cal.pop()
                cal.append(b * c)
    return cal

for tc in range(1, 11):
    length = int(input())
    calculate = list(map(str, input()))
    postfix(calculate)
    print(f'#{tc} {calculate_postfix(postfix(calculate))[0]}')
