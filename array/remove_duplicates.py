def remove_duplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i+=1
    print(nums)
    return len(nums)


nums = [0, 1, 1, 1, 2, 2, 6, 8, 10, 10, 12, 12]
length = remove_duplicates(nums)
print(length)