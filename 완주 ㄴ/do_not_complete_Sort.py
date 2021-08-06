def solution(participant, completion):

    participant_sorted = sorted(participant)
    completion_sorted = sorted(completion)

    for i in range(len(completion_sorted)):
        if participant_sorted[i] != completion_sorted[i]:
            return participant_sorted[i]

        # 알파벳 순서로 마지막 사람이 완주를 못했을 수 있으므로
    return participant_sorted[-1]

part1 = ["leo", "kiki", "eden"]
comp1 = ["eden", "kiki"]

part2 = ['mariana', 'josipa', 'nikola', 'vinko', 'fili']
comp2 = ['josipa', 'fili', 'mariana', 'nikola']

part3 = ["mislav", "stanko", "mislav", "ana"]	
comp3 = ["stanko", "ana", "mislav"]

print(solution(part1, comp1))
print(solution(part2, comp2))
print(solution(part3, comp3))