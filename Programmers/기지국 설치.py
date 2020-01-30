def solution(n, stations, w):
    ans = 0
    if stations[0]-w > 1:
        ans += ((stations[0]-w-2)//(2*w+1))+1
    if stations[-1]+w < n:    
        ans += ((n-stations[-1]-w-1)//(2*w+1))+1
    for i in range(len(stations)-1):
        ans += ((stations[i+1]-stations[i]-2*w-2)//(2*w+1))+1
    return ans
