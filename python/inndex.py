#Input: nums = [3,2,4], target = 6
#Output: [1,2]





def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


nums = [3, 3]
target = 6
output = two_sum(nums, target)
print(output)  








