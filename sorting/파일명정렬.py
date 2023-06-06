import re

def solution(files):
    file_list = []
    for idx, file in enumerate(files):
        p = re.split('([0-9]+)', file)
        file_list.append(p)
    file_list.sort(key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(file) for file in file_list]