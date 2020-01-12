def solution(road):
    cam = 0
    road = sorted(road, key=lambda x:x[1])
    lc = -30000
    for i in road:
        if lc < i[0]:
            lc = i[1]
            cam+=1    
    return cam
