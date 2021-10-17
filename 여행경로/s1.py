
def dfs():
    global answer, total
    if len(tickets)==0:
        total.append(answer[:])
        return
    now = answer[-1]
    temp = []
    for ticket in tickets:
        if ticket[0] == now:
            temp.append(ticket[1])
    for temp1 in temp:
        answer.append(temp1)
        tickets.remove([now,temp1])
        dfs()
        answer.pop(-1)
        tickets.append([now,temp1])


def solution(tickets):
    global total, answer
    answer = ["ICN"]
    temp = []
    total = []
    dfs()
    total.sort()
    return total[0]



tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
tickets = [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
print(solution(tickets))
tickets = [["ICN","A"],["ICN","A"],["A","ICN"]]
print(solution(tickets))
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
print(solution(tickets))
tickets = [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]
print(solution(tickets))