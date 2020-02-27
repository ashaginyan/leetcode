import re
def is_palindrome(s):
  words = s.split()
  new_words = []
  for word in words:
    fa = re.findall('\w*', word.lower())
    for f in fa:
      new_words.append(f)
  words = new_words

  s = ''
  for word in words:
    s += word
  s_new = s[::-1]
  if s_new == s:
    return True
  else:
    return False

s = "a.b,."
print(is_palindrome(s))
