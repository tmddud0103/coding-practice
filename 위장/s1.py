def solution(clothes):
    clothType = {}
    for i in range(len(clothes)):
        if clothes[i][1] in clothType:
            clothType[clothes[i][1]] += 1
        else:
            clothType[clothes[i][1]] = 1
    answer = 1
    for value in clothType.values():
        answer = answer * (value + 1)
    return answer-1