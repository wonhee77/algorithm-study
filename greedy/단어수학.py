import sys

N = int(input())
dic = dict()

for _ in range(N):
    word = sys.stdin.readline().rstrip("\n")
    for i in range(len(word)):
        w = word[i]
        idx = 10 - (len(word) - i)
        if w not in dic:
            dic[w] = [0] * 10
        dic[w][idx] += 1

v = []
for k in dic.keys():
    w = dic[k]
    result = 0
    for j in range(9, -1, -1):
        result += w[j] * (10 ** (9 - j))
    v.append([k, result])

v.sort(key=lambda x: -x[1])

answer = 0
start = 9
for a in v:
    answer += a[1] * start
    start -= 1

print(answer)

'''
그리디 알고리즘 문제이다.
각 단계에서 최선의 방법을 찾아야 실행을 하는 것인데 이 문제에서의 최선의 방법은
가장 높은 자리 숫자가 높은 순으로 알파벳을 정하는 것이다.
가장 높은 숫자 자리에 알파벳 개수가 동일하게 있을 경우 그 다음 자리수에서 높은 알파벳이 높은 숫자의 선점권을 가진다.
이때 알파벳별로 각자리수의 개수를 숫자로 기록을 해둔다면 이 숫자의 오름차순대로가 전체를 더했을 때 가장 큰 값이 나오게 된다.
'''