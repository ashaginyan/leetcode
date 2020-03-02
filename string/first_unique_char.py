def first_unique_char(s):
  counts = {}
  for letter in s:
    if letter in counts:
      counts[letter] += 1
    else:
      counts[letter] = 1
  
  for letter in s:
    if counts[letter] == 1:
      return s.index(letter)
  return -1

s = "loveleetcode"
print(first_unique_char(s))
