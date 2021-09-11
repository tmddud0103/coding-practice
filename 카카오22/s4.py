fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
def solution(fees, records):
    save = {}
    fee_save = {}
    answer = []
    for i in range(len(records)):
        if records[i][-1] == 'N':
            save[records[i].split()[1]] = records[i].split()[0]
            if records[i].split()[1] in fee_save:
                pass
            else:
                fee_save[records[i].split()[1]] = 0
        if records[i][-1] == 'T':
            in_car = save[records[i].split()[1]].split(':')
            out_car = records[i][0:5].split(':')
            time = 60 * (int(out_car[0]) - int(in_car[0])) + (int(out_car[1]) - int(in_car[1]))
            del save[records[i].split()[1]]
            fee_save[records[i].split()[1]] += time

    for key, value in save.items():
        value.split(':')
        time = 60 * (23 - int(value.split(':')[0])) + (59 - int(value.split(':')[1]))
        fee_save[key] += time
    sfee = sorted(fee_save.items())
    for t in range(len(sfee)):
        if sfee[t][1] <= fees[0]:
            answer.append(fees[1])
        else:
            money = ((sfee[t][1]-fees[0])//fees[2]) * fees[3]
            print(money)
            if (sfee[t][1]-fees[0]) % fees[2] != 0:
                money += fees[3]
                print(money)
            answer.append(money + fees[1])



    return answer









print(solution(fees, records))