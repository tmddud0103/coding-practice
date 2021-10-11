from collections import deque
def solution(begin, target, words):
    length = len(begin)
    graph = deque([[begin, 0]])
    already = [] #쓴
    while words:
        next_words=[] #쓸
        current, i = graph.pop()
        if current not in already:
            already.append(current)
            if i != 0:
                words.remove(current)
            if len(words)==0:
                return 0
            if current == target:
                return i
            else:
                for word in words:
                    mismatched=0
                    # if len([c for c, _ in graph if c == word]) != 0:
                    #     continue
                    for j in range(length):
                        if current[j] != word[j]:
                            mismatched+=1
                    if mismatched == 1:
                        next_words.append([word, i+1])
        graph.extend(next_words)
        if len(graph) == 0:
            return 0
    return 0