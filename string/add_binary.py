def bin_to_int(a):
  a = a[::-1]
  power = len(a) - 1
  i = 0
  while power >= 0:
    i = int(a[power])*2**power + i
    power -= 1
  return i

def int_to_bin(a):
  s = ''
  carry = 0
  if a == 0:
    return '0'
  while carry <= a:
    carry = a % 2
    a = a // 2
    s += str(carry)
  return s[::-1]

def add_binary(a, b):
  a = bin_to_int(a)
  b = bin_to_int(b)
  res = a + b
  res = int_to_bin(res)
  return res

a = '1010'
b = '1011'
print(add_binary(a, b))
