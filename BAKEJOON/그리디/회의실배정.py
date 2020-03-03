ans = 1
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

#회의 일찍끝나는순 + 일찍 끝나는 순
arr = sorted(arr, key = lambda x:(x[1],x[0]))

end = arr[0][1]
arr.pop(0)

for h in arr:
    if end <= h[0]:
        end = h[1]
        ans += 1
print(ans)
