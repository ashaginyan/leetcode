def reverse_vowels(s):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  vowels_s = ''
  vowels_i = []
  s_l = []
  for i, letter in enumerate(s):
    s_l.append(letter)
    if letter in vowels:
      vowels_i.append(i)
      vowels_s += letter
  
  vowels_s = vowels_s[::-1]
  for k, ind in enumerate(vowels_i):
    s_l[ind] = vowels_s[k]

  return ''.join(s_l)

s = "aA"
reverse_vowels(s)
