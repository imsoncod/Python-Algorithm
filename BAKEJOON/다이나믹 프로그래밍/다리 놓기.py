from math import factorial
T = int(input())
for _ in range(T):
    n, m = input().split()
    n = int(n)
    m = int(m)
    print(factorial(m)//factorial(m-n)//factorial(n)) #조합
