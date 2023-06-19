from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        candidate = []
        for order in orders:
            candidate += (combinations(sorted(order), i))
        counter = Counter(candidate)
        if len(counter) >= 1 and max(counter.values()) >= 2:
            for j in counter:
                if counter[j] == max(counter.values()):
                    answer += [''.join(j)]
    return sorted(answer)


'''
combination() 순서를 고려하지 않고 중복없이 뽑는 경우의 수
Counter() 숫자를 세어 map 형식으로 return
'''