import sys

dic = dict()
total = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if tree == '':
        break
    total += 1
    if tree not in dic:
        dic[tree] = 1
    else:
        dic[tree] += 1

trees = []

for key in dic.keys():
    trees.append((key, dic[key]))

trees.sort()

for t in trees:
    print(t[0], end=' ')
    percent = t[1] / total * 100
    print('%.4f' % percent)
