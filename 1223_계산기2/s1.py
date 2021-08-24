import sys
sys.stdin = open('input.txt')

# 후위표기식
def postfix(asd):
    total = ''
    temp = []
    for i in range(0, length):
        try:
            a = int(asd[i])
            total += str(a)
        except:
            if len(temp) == 0:
                temp.append(asd[i])
                # 후위 표기식 진짜 어렵다
                # +, * 두개 밖에 없는데도 이렇게 까다로운데
                # 사칙연산에 괄호 있으면 어캐푸누...?
            else:
                if temp[-1] == '+' and asd[i] == '*':
                    temp.append(asd[i])

                elif temp[-1] == '+' and asd[i] == '+':
                    total += asd[i]

                elif temp[-1] == '*' and asd[i] == '*':
                    total += asd[i]

                elif temp[-1] == '*' and asd[i] == '+':
                    if len(temp) == 2:
                        temp.pop()
                        total += '*'
                        temp.pop()
                        total += '+'
                        temp.append(asd[i])
                    else:
                        temp.pop()
                        total += '*'
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
    for i in range(0, length):
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
    print(postfix(calculate))
    print(f'#{tc} {calculate_postfix(postfix(calculate))[0]}')