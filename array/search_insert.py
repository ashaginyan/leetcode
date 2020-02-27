def search_insert(nums, target):
  i = 0
  el = nums[i]
  while el < target:
    if target > nums[len(nums) - 1]:
      return len(nums)
    else:
      i += 1
      el = nums[i]
  return i

nums = [1]
target = 1
print(search_insert(nums, target))
