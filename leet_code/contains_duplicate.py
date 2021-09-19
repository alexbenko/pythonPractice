def contains_duplicate(nums: [int]) -> bool:
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] = counter[num] + 1
        else:
            counter[num] = 1

    for num in counter:
        if counter[num] > 1:
            return True

    return False


print(contains_duplicate([1,2,3,1])) # => True
print(contains_duplicate([1,2,3,4])) # => False
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2])) #=> True