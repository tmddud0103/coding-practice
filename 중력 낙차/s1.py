import sys
sys.stdin = open('input.txt')

# 낙차 계산
def calculating_falling_box(height_of_the_tallest_box, rooms_of_boxes):
    height_fall_one_box = 0 #한 박스가 떨어지는 높이
    highest_fall_height = 0 #가장 많이 떨어지는 박스의 높이
    for x_line in range(height_of_the_tallest_box, 0, -1):
        fallen_count = 0  # 떨어지는 높이
        safe_box_count = 0  # 밑에서 막아주는 박스 갯수
        for x_axis_reverse in rooms_of_boxes[::-1]:
            if x_line > x_axis_reverse:
                fallen_count += 1
            else:
                height_fall_one_box = fallen_count - safe_box_count
                fallen_count += 1
                safe_box_count += 1
                if height_fall_one_box > highest_fall_height:
                    highest_fall_height = height_fall_one_box
    return highest_fall_height

# 제일 높은 박스의 높이 찾기
def who_is_tallest(rooms_of_boxes):
    result = 0
    for x in rooms_of_boxes:
        if x > result:
            result = x
    return result

# 전체 코드를 몇번 반복할지 input을 이용해서 값을 가져옴
test_case = int(input())

#실제 계산
for times in range(test_case):
    num_of_rooms = int(input())
    rooms_of_boxes = list(map(int, input().split()))
    height_of_the_tallest_box = who_is_tallest(rooms_of_boxes) #가장 높은 박스의 높이
    print(calculating_falling_box(height_of_the_tallest_box, rooms_of_boxes))
