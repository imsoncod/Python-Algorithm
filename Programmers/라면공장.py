import heapq

def solution(stock, dates, supplies, k):
    ans = 0
    hq = []
    idx = 0
    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(hq, -supplies[i])
            idx += 1
        stock += heapq.heappop(hq)*-1
        ans+=1
    return ans
