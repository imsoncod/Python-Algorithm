import math
#하나의 숫자 소수 판별

def is_prime_number(x):
    #판별하고자 하는 수의 제곱근까지만 나눠봐도 소수를 판별할 수 있다
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

#다수의 숫자 소수 판별
#특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 할 경우
#에라토스테네스의 체

#2부터 1000사이의 모든 소수 찾기
n = 1000
array = [True for _ in range(n+1)]

for i in range(2, int(n**0.5) + 1):
    if array[i] == True:
        j = 2 #i에 곱해질 값(배수)
        while i * j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
