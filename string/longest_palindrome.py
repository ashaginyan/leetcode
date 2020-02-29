def longest_palindrome(s):
  s_pal = ''
  s = s + ' '
  for i in range(len(s)):
    for j in range(len(s)):
      s1 = s[i:j]
      if s1 == s1[::-1] and len(s1) > len(s_pal):
        s_pal = s1
  return s_pal

s = "b"
print(longest_palindrome(s))
