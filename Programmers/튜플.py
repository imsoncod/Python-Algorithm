import re
from collections import Counter

def solution(s):
    #정규표현식
    arr = Counter(re.findall('\d+',s))
    return list(map(int, [k for k, v in sorted(arr.items(), key=lambda x:-x[1])]))
