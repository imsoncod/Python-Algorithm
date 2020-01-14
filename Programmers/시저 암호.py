import string

def solution(s, n):
    up = string.ascii_uppercase
    down = string.ascii_lowercase
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        elif c in up:
            idx = up.index(c)+n
            if idx > 25:
                idx = idx - 26
            answer += up[idx]
        elif c in down:
            idx = down.index(c)+n
            if idx > 25:
                idx = idx - 26
            answer += down[idx]
    return answer
