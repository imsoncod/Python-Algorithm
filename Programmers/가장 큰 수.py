def solution(numbers):
    s = list(map(str,numbers))
    s.sort(key=lambda k:k*3, reverse=True)
    return ''.join(s)
