def solution(weight):
    weight.sort()
    s=1
    for i in range(len(weight)):
        if s < weight[i]:
            break
        s+=weight[i]
    return s
