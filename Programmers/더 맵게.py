import heapq

def solution(s, K):
    heapq.heapify(s)
    cnt=0
    while s[0]<K:
        try:
            a = heapq.heappop(s)
            b = heapq.heappop(s)
            heapq.heappush(s,a+b*2)
        except IndexError:
            return -1            
        cnt+=1
    return cnt
