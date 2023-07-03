N = int(input())
people = list(map(int, input().split()))

people.sort()

answer = 0
for i in range(len(people)):
    answer += people[i] * (len(people) - i)

print(answer)

