import sys
sys.stdin = open('input.txt')
# test_case = int(input())
# 테스트 케이스는 10개

test_case = 10
for tc in range(1, test_case + 1):
    number_of_dump = int(input())
    building_of_box = list(map(int, input().split()))
    for times in range(number_of_dump):
        max_height = building_of_box[0]
        max_box_number = 0
        min_height = building_of_box[0]
        min_box_number = 0
        for i in range(1, 100):
            if building_of_box[i] > max_height:
                max_height = building_of_box[i]
                max_box_number = i
            if min_height > building_of_box[i]:
                min_height = building_of_box[i]
                min_box_number = i
        building_of_box[max_box_number] -= 1
        building_of_box[min_box_number] += 1
    max_height = building_of_box[0]
    min_height = building_of_box[0]
    for i in range(1, 100):
        if building_of_box[i] > max_height:
            max_height = building_of_box[i]
        if min_height > building_of_box[i]:
            min_height = building_of_box[i]
    print('#{} {}'.format(tc, max_height - min_height))