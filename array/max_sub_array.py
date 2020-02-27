def max_sub_array(nums):
  """Kardane's algorithm"""
  current_sum = 0
  best_sum = float('-inf')
  for num in nums:
    current_sum = max(num, current_sum + num)
    best_sum = max(current_sum, best_sum)
  return best_sum

nums = [-5, -5, 0, 9, 1, -2, 4 -2, -1]
print(max_sub_array(nums))
