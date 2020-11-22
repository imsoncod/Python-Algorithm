#풀이1
#10진수를 n진수로 변환하는 함수
def convert(n, base):
    temp = "0123456789ABCDE"
    q, r = divmod(n, base)
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + str(r)

def solution(n):
    convert_num = convert(n, 3)[::-1]

    return int(convert_num, 3)

#풀이2
def solution(n):
    convertNum = ""
    
    while n > 0:
        convertNum += str(n%3)
        n //= 3
    
    return int(convertNum, 3)
    
#int(문자열, n) : n진수로 이루어진 문자열을 10진수로 변환한다
