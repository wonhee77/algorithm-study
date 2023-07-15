N = int(input())
nums = list(map(int, input().split()))
nums.sort()
total = 1

for i in range(len(nums)):
    num = nums[i]
    if num > total:
        break
    total += num

print(total)
