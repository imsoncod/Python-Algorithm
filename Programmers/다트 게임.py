def solution(dart):
    answer = []
    temp = 0
    dart = dart.replace('10','@')
    for i in dart:
        if i.isdigit():
            answer.append(temp)
            temp = 0
            temp += int(i)
        else:
            if i == '@':
                answer.append(temp)
                temp = 0
                temp += 10
            elif i == 'S':
                temp **= 1
            elif i == 'D':
                temp **= 2
            elif i == 'T':
                temp **= 3
            elif i == '#':
                temp *= -1
            elif i == '*':
                temp *= 2
                answer[-1] *= 2
    answer.append(temp)            
    return sum(answer)
