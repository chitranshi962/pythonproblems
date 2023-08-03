#Input: nums = [3,3], target = 6
#Output: [0,1]





def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i


nums = [3, 2, 4]
target = 6
result = two_sum(nums, target)
print(result)  






