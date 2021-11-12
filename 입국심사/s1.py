# import heapq
def solution(n, times):
    # a = 0
    # total = []
    # for time in times:
    #         heapq.heappush(total, [time, time])
    # while a != n:
    #     a += 1
    #     b, k =heapq.heappop(total)
    #     heapq.heappush(total, [b+k, k])
    # return b
    high = max(times) * n
    low = 1

    def binarySearch(high, low, times, n):
        answer = 0
        while low <= high:
            cnt = 0
            mid = (low + high) // 2
            for time in times:
                cnt += mid // time
            if cnt >= n:
                if answer == 0:
                    answer = mid
                else:
                    answer = min(answer, mid)
                high = mid - 1
            elif cnt < n:
                low = mid + 1
        return answer

    answer = binarySearch(high, low, times, n)
    print(answer)
    return answer