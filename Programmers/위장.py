import collections

def solution(clothes):
    answer = 1
    a = list((collections.Counter(x[1] for x in clothes)).values())
    for i in a:
        answer *= (i+1)
    return answer-1
