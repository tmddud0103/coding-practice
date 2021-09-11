import sys
sys.stdin = open('input.txt')

TC = int(input())

def solution(new_id):
    # 1단계 소문자 치환
    new_id = new_id.lower()
    answer = ''
    for i in range(len(new_id)):
        # 2단계 알파벳 숫자 - _ . 제외한 모든 문자 제거
        if new_id[i].isalnum() or new_id[i] == '-' or new_id[i] == '_':
            answer += new_id[i]
        elif new_id[i]=='.' and len(answer) == 0:
            answer += new_id[i]
        # 3단계 연속된 . 제거
        elif new_id[i]=='.':
            if answer[-1] == '.':
                pass
            else:
                answer += new_id[i]
        else: pass

    # 4단계 처음과 끝의 . 제거
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계 a 대입
    if len(answer) == 0:
        answer += 'a'
    # 6단계 16자 이상이면 15자만
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계 3자리가 될때까지 마지막 문자 반복
    if len(answer) < 3:
        while len(answer) != 3:
            answer += answer[-1]
    return answer



for tc in range(1, TC + 1):
    new_id = str(input())
    print(solution(new_id))