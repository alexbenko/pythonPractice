def two_sum(nums: [int], target: int) -> [int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum([2,7,11,15], 9)) #=> [0,1]

