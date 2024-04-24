def reverse_words(s: str) -> str:
    # lol
    sanitized = s.split()
    return ' '.join(sanitized[::-1])