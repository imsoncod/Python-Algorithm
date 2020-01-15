from math import gcd
def solution(arr):
    n = arr.pop(0)
    for i in arr:
        n = n*i//gcd(n,i)
    return n
