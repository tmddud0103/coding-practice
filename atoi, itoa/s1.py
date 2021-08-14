def itoa(number):
    make_a = []
    while number > 10:
        a = number % 10
        make_a.append(a)
        number = number // 10
    make_a.append(number)
    n = ''
    for i in range(len(make_a) - 1, -1, -1):
        n += '{}'.format(make_a[i])
    return n

def atoi(string):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = 0
    for i in range(0, len(string)):
        for j in numbers:
            if string[i] == '{}'.format(numbers[j]):
                value = value * 10 + numbers[j]
    return value

print(type(itoa(1234)))
print(type(atoi('1234')))
print(itoa(1234))
print(atoi('1234'))