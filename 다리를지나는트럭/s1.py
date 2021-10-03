def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_time = []
    bgsum = 0
    while len(bridge_time) != 0 or len(truck_weights) != 0:
        time += 1
        for i in range(len(bridge_time)):
            bridge_time[i][1] += 1
        if len(bridge_time) != 0 and bridge_time[0][1] == bridge_length:
            a = bridge_time.pop(0)
            bgsum -= a[0]

        if len(truck_weights) != 0:
            if bgsum + truck_weights[0] <= weight:
                temp_truck = truck_weights.pop(0)
                bridge_time.append([temp_truck, 0])
                bgsum += temp_truck

    return time

bridge_length =2
weight =10
truck_weights =[7,4,5,6]
print(solution(bridge_length, weight, truck_weights))
bridge_length =100
weight =100
truck_weights =[10]
print(solution(bridge_length, weight, truck_weights))
bridge_length =100
weight =100
truck_weights =[10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))
bridge_length =5
weight =5
truck_weights =[2, 2, 2, 2, 1, 1, 1, 1, 1]
print(solution(bridge_length, weight, truck_weights))