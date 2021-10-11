def solution(prices):
    N = len(prices)
    answer = [0] * N
    for i in range(0, N):
        if prices[i] == 1:
            answer[i] = N-1-i
        else:
            for j in range(i+1, N):
                if prices[i] > prices[j]:
                    answer[i] = j - i
                    break
            if answer[i] == 0:
                answer[i] = N - 1 - i
    return answer