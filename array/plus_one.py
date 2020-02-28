def plus_one(digits):
  s = ''
  for digit in digits:
    s += str(digit)
  digits = list(str(int(s) + 1))
  digits = [int(digit) for digit in digits]
  return digits

digits = [1, 9, 9]
print(plus_one(digits))
