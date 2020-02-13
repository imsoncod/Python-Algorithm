from math import gcd
def solution(w,h):
    return (w-1)*(h-1) if gcd(w,h)==1 else w*h-w-h+gcd(w,h)
