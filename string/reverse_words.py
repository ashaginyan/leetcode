def reverse_words(s):
    words = s.split()
    words = [word.strip() for word in words]
    words = words[::-1]
    return ' '.join(words)
