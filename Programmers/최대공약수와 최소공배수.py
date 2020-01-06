from math import gcd

def solution(n, m):
    arr = [gcd(n,m), n*m//gcd(n,m)]
    return arr
