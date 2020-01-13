"""절단부위를 !로 바꾼 후 규칙을 구해보자"""
def solution(arr):
    a = 0   # "("의 개수
    answer = 0
    arr = arr.replace("()","!") # "()"을 "!"로 바꿈
    for i in arr:
        if i == "(": # "("일 경우 "("의 개수와 answer 를 +1
            a += 1
            answer += 1
        elif i == "!": # "!"일 경우 "("의 개수만큼 answer를 +
            answer += a
        elif i == ")": # ")"일 경우 "("의 개수를 -1
            a -= 1
    return answer
