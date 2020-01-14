def solution(s):
    return ' '.join(w.capitalize() for w in s.lower().split(" "))
