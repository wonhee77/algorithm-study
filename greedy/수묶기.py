N = int(input())

plus = []
zero = 0
minus = []

for _ in range(N):
    num = int(input())
    if num > 0:
        plus.append(num)
    elif num == 0:
        zero += 1
    else:
        minus.append(num)

answer = 0

plus.sort(reverse=True)
plus_limit = len(plus)
if len(plus) % 2 != 0:
    plus_limit -= 2
    answer += plus[-1]

for i in range(0, plus_limit, 2):
    if plus[i] * plus[i + 1] == plus[i]:
        answer += plus[i] + plus[i + 1]
        continue
    answer += (plus[i] * plus[i + 1])


minus.sort()
minus_limit = len(minus)
if len(minus) % 2 != 0:
    minus_limit -= 2
    if zero == 0:
        answer += minus[-1]

for i in range(0, minus_limit, 2):
    answer += (minus[i] * minus[i + 1])

print(answer)






