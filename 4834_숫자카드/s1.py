import sys
sys.stdin = open('input.txt')

test_case = int(input())
for test in range(1, test_case + 1):
    number_of_card = int(input())
    list_of_cards = str(input())
    count = 0
    max_count = 0
    max_number = 0
    #카드의 갯수가 같으면 높은 카드를 출력해야하니 높은 숫자부터 확인한다
    for i in range(9, -1, -1):
        for number in list_of_cards:
            if i == int(number):
                count += 1
            #카드의 갯수가 같을 경우 높은 숫자의 카드부터 진행해서 신경 쓸 필요 없다
            if count > max_count:
                max_count = count
                max_number = i
        count = 0
    print('#{} {} {}'.format(test, max_number, max_count))