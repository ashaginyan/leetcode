def two_sum_II(numbers, target):
  left = 0
  right = len(numbers)-1
  while left < right:
    sum_ = numbers[left] + numbers[right]
    if sum_ == target:
      return [left+1, right+1]
    if sum_ > target:
      right -= 1
    if sum_ < target:
      left += 1

numbers = [0, 0, 11, 15]
target = 0

two_sum_II(numbers, target)
