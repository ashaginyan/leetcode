def roman_to_int(s):
  patterns = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
  letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  sum_ = 0
  s_new = s

  for i in range(0, len(s)):
    if i != len(s)-1:
      try:
        if s[i:i+2] in patterns:
          sum_ += patterns[s[i:i+2]]
          first_ind = s_new.index(s[i])
          s_new = s_new[:first_ind] + s_new[first_ind+2:]
      except:
        pass

  for letter in s_new:
    sum_ += letters[letter]

  return sum_

print(roman_to_int(s='III'))
