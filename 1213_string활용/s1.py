import sys
sys.stdin = open('input.txt')

# test_case = int(input())
# for tc in range(1, test_case + 1):

for tc in range(1, 11):
    test_case = int(input())
    find_word = str(input())
    sentence = list(map(str, input()))
    answer = 0
    for i in range(0, len(sentence) -len(find_word)+ 1):
        if sentence[i] == find_word[0]:
            check = 0
            len_find_word = len(find_word)
            for j in range(0, len(find_word)):
                if i + j < len(sentence):
                    if sentence[i + j] == find_word[j]:
                        check += 1
                        if check == len_find_word:
                            answer += 1
    print('#{} {}'.format(test_case, answer))
