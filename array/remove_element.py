def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(val)
        else:
            i += 1
    print(nums)
    return len(nums)


nums = [0, 2, 0, 5, 1, 3, 0, 4, 0]
val = 0
print(remove_element(nums, val))