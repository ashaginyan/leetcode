def reverse_string(s):
  for i in range(len(s)//2):
    left = s[i]
    s[i] = s[-i-1]
    s[-i-1] = left
  print(s)

s = ["h","e","l","l","o"]
reverse_string(s)
