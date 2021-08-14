def itoa(my_int):
    my_str = []
    while my_int != 0:
        r = my_int % 10
        #숫자를 아스키코드로 바꾸고 그 코드를 다시 숫자(문자)로 바꾼다
        char = chr(r + ord('0'))
        my_str.append(char)
        my_int //= 10
    my_str.reverse()
    result = ''.join(my_str)
    return result


def atoi(my_str):
    value = 0
    i = 0
    while i < len(my_str):
        char = my_str[i]
        digit = ord(char) - ord('0')
        value = value * 10 + digit
        i += 1
    return value


print(itoa(123))
print(type(itoa(123)))
print(atoi('1234'))