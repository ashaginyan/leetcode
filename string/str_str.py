def str_str(haystack, needle):
  window = len(needle)
  if window == 0:
    return 0
  for i in range(len(haystack) - window + 1):
    if haystack[i:i + window] == needle:
      return i
  return -1

haystack = "a"
needle = "a"
print(str_str(haystack, needle))
