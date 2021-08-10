import sys
sys.stdin = open('input.txt')

test_case = int(input())
file_output = open("output.txt", "w")
for test in range(1, test_case + 1):
    number_of_numbers = int(input())
    list_of_numbers = list(map(int, input().split()))
    max_number = 0;
    min_number = 1000000;
    for i in range(number_of_numbers):
        if list_of_numbers[i] > max_number:
            max_number = list_of_numbers[i]
        if list_of_numbers[i] < min_number:
            min_number = list_of_numbers[i]
    result = '#{} {}'.format(test, max_number - min_number)
    print(result)
    file_output.write('#{} {}\n'.format(test, max_number - min_number))
file_output.close()

# print('{}, {}, {}'.format(test, number_of_numbers, list_of_numbers))
# numbers = list(map(int, input().split()))
