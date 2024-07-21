def twoSum(nums, target):
    num_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[nums[i]] = i
    return []

num = [3,2,4]
target1 = 6
print(twoSum(nums=num,target=target1))