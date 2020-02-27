def is_valid(s):
  while '()' in s or '{}' in s or '[]' in s:
    s = s.replace('()', '')
    s = s.replace('{}', '')
    s = s.replace('[]', '')
  if s != '':
    return False
  else:
    return True

s = "{[({)]}"
print(is_valid(s))
