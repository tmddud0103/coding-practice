import sys
sys.stdin = open('input.txt')

def word_to_number(count, word):
    w_to_num = []
    for i in range(0, count):
        if word[i] == 'ZRO':
            w_to_num.append('0')
        elif word[i] == 'ONE':
            w_to_num.append('1')
        elif word[i] == 'TWO':
            w_to_num.append('2')
        elif word[i] == 'THR':
            w_to_num.append('3')
        elif word[i] == 'FOR':
            w_to_num.append('4')
        elif word[i] == 'FIV':
            w_to_num.append('5')
        elif word[i] == 'SIX':
            w_to_num.append('6')
        elif word[i] == 'SVN':
            w_to_num.append('7')
        elif word[i] == 'EGT':
            w_to_num.append('8')
        elif word[i] == 'NIN':
            w_to_num.append('9')
        else:
            print('wrong')
            return
    return w_to_num
def number_to_word(count, number):
    num_to_wo = []
    for i in range(0, count):
        if number[i] == '0':
            num_to_wo.append('ZRO')
        elif number[i] == '1':
            num_to_wo.append('ONE')
        elif number[i] == '2':
            num_to_wo.append('TWO')
        elif number[i] == '3':
            num_to_wo.append('THR')
        elif number[i] == '4':
            num_to_wo.append('FOR')
        elif number[i] == '5':
            num_to_wo.append('FIV')
        elif number[i] == '6':
            num_to_wo.append('SIX')
        elif number[i] == '7':
            num_to_wo.append('SVN')
        elif number[i] == '8':
            num_to_wo.append('EGT')
        elif number[i] == '9':
            num_to_wo.append('NIN')
        else:
            print('wrong')
            return
    return num_to_wo


test_case = int(input())
for tc in range(1, test_case + 1):
    test_number, count = list(map(str, input().split()))
    count = int(count)
    number_list = list(map(str, input().split()))
    wo_num = word_to_number(count, number_list)
    wo_num.sort()
    result = number_to_word(count, wo_num)
    print(test_number)
    for i in range(0, count):
        print(result[i], end=' ')
    print()
