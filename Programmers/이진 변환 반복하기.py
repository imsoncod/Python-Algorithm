#풀이1
def solution(s):
    cnt = 0
    zero_sum = 0

    while s != '1':
        zero = s.count('0')
        c = len(s)-zero
        temp = ""
        while c > 0:
            temp += str(c%2)
            c //= 2
        s = temp
        cnt += 1
        zero_sum += zero    

    return [cnt, zero_sum]

#풀이2
#bin을 이용한 10진수 -> 2진수 변환
#bin메소드는 리턴값 앞에 '0b'라는 문자가 붙음으로 제거해준다
def solution(s):
    a, b = 0, 0
    
    while s != '1':
        a += 1
        one = s.count('1')
        b += len(s) - one
        s = bin(one)[2:]
    
    return [a, b]
