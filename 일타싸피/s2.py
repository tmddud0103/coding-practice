import math
balls =[[50, 70],[10, 30]]
holes=[[0,127],[127,127],[254,127],[0,0],[127,0],[254,0]]
white_ball = balls[0]
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


x = abs(hole[0] - white_ball[0])
y = abs(hole[1] - white_ball[1])
a = (x**2 + y**2)**(1/2)
r = 5.72
b = ((hole[0] - ball[0])**2 + (hole[1] - ball[1])**2)**(1/2)
c = ((white_ball[0] - ball[0])**2 + (white_ball[1] - ball[1])**2)**(1/2)
angle_c = math.acos((-c**2 + a**2 + b**2)/(2*a*b))
d = ((a* math.sin(angle_c))**2 + (b+r-(a*math.cos(angle_c)))**2)**(1/2)
theta_double_prime = math.acos((d**2 + a**2 - (b+r)**2)/(2*a*d))
theta_prime = math.atan(x/y)
theta = theta_prime + theta_double_prime
theta = math.degrees(theta)

print(theta + 180)
