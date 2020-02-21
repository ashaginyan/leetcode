def two_sum(nums, target):
    d = {}
    for num in nums:
        d[num] = num
    for i, num in enumerate(nums):
        dif = target - num
        if dif in d:
            first_ind = i
            second_ind = nums.index(dif)
            if first_ind != second_ind:
                return [first_ind, second_ind]


nums = [0, 4, 3, 0]
target = 0


indices = two_sum(nums, target)
print(indices)