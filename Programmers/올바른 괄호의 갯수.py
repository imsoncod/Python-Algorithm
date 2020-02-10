#카탈란수...라는게 있다고한다
from math import factorial as fac
def solution(n):
    return fac(2*n)/(fac(n+1)*fac(n))
