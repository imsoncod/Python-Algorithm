def solution(a, b):
    date = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    d = b
    for i in range(a):
        d+=date[i]
    return day[d%7]
