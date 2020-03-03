def longest_common_prefix(strs):
  if strs == []:
    return ''
  lens = []
  for s in strs:
    lens.append(len(s))
  len_min = min(lens)
  i = len_min
  while i >= 0:
    set_strs = set([str_[:i] for str_ in strs])
    if len(set_strs) == 1:
      return set_strs.pop()
    else:
      i -= 1
  return ''


strs = ["dog","racecar","car"]
longest_common_prefix(strs)
