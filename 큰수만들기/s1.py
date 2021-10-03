

def solution(number, k):
    noOfReturn = len(number) - k
    answer = ''
    temp1 = -1
    for _ in range(noOfReturn):
        j = '0'
        for i in range(temp1+1, k+len(answer)+1):
            if number[i] > j:
                j = number[i]
                temp1 = i
                if j == '9':
                    break
        answer += j


    return answer



# def solution(number, k):
#     noOfReturn = len(number) - k
#     answer = ' '
#     while noOfReturn:
#         temp1 = number.find(answer[-1])
#         number = number[temp1+1:]
#         temp = list(number[0:len(number) - noOfReturn+1])
#         temp.sort(reverse=True)
#         answer += temp[0]
#         noOfReturn -= 1
#     return answer[1:]

number = "1924"
k = 2
print(solution(number, k))
number = "1231234"
k = 3
print(solution(number, k))
number = "4177252841"
k = 4
print(solution(number, k))