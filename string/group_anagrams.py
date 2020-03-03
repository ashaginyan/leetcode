def group_anagrams(strs):
  d = {}
  for s in strs:
    key = tuple(sorted(s))
    d.setdefault(key, [])
    d[key].append(s)
  return list(d.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
