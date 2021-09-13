import math
balls =[[50, 70],[10, 30]]
holes=[[0,127],[127,127],[254,127],[0,0],[127,0],[254,0]]

# 공 직경 : 5.72
if balls[1][0] != -1:
    # 집어넣을 구멍 찾기
    ball = balls[1]
    if balls[1][0] > 63:
        if balls[1][1] <= 63:
            hole = holes[0]
        elif balls[1][1] <= 190:
            hole = holes[1]
        else:
            hole = holes[2]
    else:
        if balls[1][1] <= 63:
            hole = holes[3]
        elif balls[1][1] <= 190:
            hole = holes[4]
        else:
            hole = holes[5]

    # 집어 넣을 공과 구멍에 대한 기울기 구하기
slope = ball[1] - hole[1] / ball[0] - hole[0]
distance = ((ball[1] - hole[1])**2 + (ball[0] - hole[0])**2)**(1/2)
dis_x = (abs(hole[0]-ball[0])*(5.72))/distance
dis_y = (abs(hole[1]-ball[1])*(5.72))/distance

# 1사분면
if hole[1] - ball[1] > 0 and hole[0] - ball[0] > 0:
    go_to_x = ball[0] - dis_x
    go_to_y = ball[1] - dis_y
# 2사분면
elif hole[1] - ball[1] < 0 and hole[0] - ball[0] > 0:
    go_to_x = ball[0] + dis_x
    go_to_y = ball[1] - dis_y
# 3사분면
elif hole[1] - ball[1] < 0 and hole[0] - ball[0] < 0:
    go_to_x = ball[0] + dis_x
    go_to_y = ball[1] + dis_y
# 4사분면
elif hole[1] - ball[1] > 0 and hole[0] - ball[0] < 0:
    go_to_x = ball[0] - dis_x
    go_to_y = ball[1] + dis_y
# y값의 변화 = 0
else:
    go_to_x = ball[0]
    go_to_y = ball[1] + 5.72

white_ball = balls[0]
x = white_ball[0] - go_to_x
y = white_ball[1] - go_to_y
print(x, y)
if x < 0 and y < 0:
    degree = math.degrees(math.atan(y/x))
    degree = 90 - degree
elif x > 0 and y < 0:
    degree = math.degrees(math.atan(abs(y/x)))
    degree = 90 + degree
elif x > 0 and y > 0:
    degree = math.degrees(math.atan(abs(y / x)))
    degree = 270 - degree

else:
    degree = math.degrees(math.atan(abs(y / x)))
    degree = 270 + degree
print('degree', degree)