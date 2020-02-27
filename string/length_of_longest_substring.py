def length_of_longest_substring(s):
  maximum = 0
  for j in range(len(s)):
    st = ''
    i = j
    while s[i:i+1] not in st:
      st = st + s[i:i+1]
      print(st)
      i += 1
    if len(st) > maximum:
      maximum = len(st)
  return maximum

s = 'dvdf'
print(length_of_longest_substring(s))
