def solution(sticker):
    total_size = len(sticker)
    if total_size == 1:
        return max(sticker)

    dp_first = [0 for _ in range(total_size)]
    dp_first[0] = sticker[0]
    dp_first[1] = sticker[0]
    dp_second = [0 for _ in range(total_size)]
    dp_second[1] = sticker[1]
    dp_second[2] = sticker[1]

    for i in range(2, total_size - 1):
        dp_first[i] = max(dp_first[i - 1], dp_first[i - 2] + sticker[i])

    for i in range(3, total_size):
        dp_second[i] = max(dp_second[i - 1], dp_second[i - 2] + sticker[i])

    return max(dp_first[-2], dp_second[-1])