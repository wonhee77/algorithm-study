import heapq
import math

def to_minutes(time):
    t = time.split(":")
    return int(t[0]) * 60 + int(t[1])

def get_fee(time, fee):
    if time <= fee[0]:
        return fee[1]
    else:
        return fee[1] + math.ceil((time - fee[0]) / fee[2]) * fee[3]

def solution(fees, records):
    last_time = to_minutes("23:59")
    dic = dict()
    for record in records:
        r = record.split(" ")
        minutes = to_minutes(r[0])
        car_num = r[1]
        if car_num in dic:
            dic[car_num].append(minutes)
        else:
            dic[car_num] = [minutes]

    heap = []

    for key in dic.keys():
        times = dic[key]
        if len(times) % 2 == 1:
            times.append(last_time)
        total_time = 0
        for i in range(0, len(times), 2):
            total_time += times[i + 1] - times[i]
        heapq.heappush(heap, (key, get_fee(total_time, fees)))

    answer = []
    while heap:
        answer.append(heapq.heappop(heap)[1])

    return answer