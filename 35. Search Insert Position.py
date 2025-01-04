nums = [int(i) for i in input().split()]
target = int(input())

if target in nums: print(nums.index(target))
else:
    for i in range(len(nums)):
        if nums[i] > target:
            print(i)
            break
        elif i == len(nums) - 1:
            print(i + 1)
            break