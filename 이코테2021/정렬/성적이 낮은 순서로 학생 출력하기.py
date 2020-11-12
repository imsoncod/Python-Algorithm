n = int(input())
arr = []

for _ in range(n):
    data = input().split()
    arr.append([data[0], int(data[1])])

arr = sorted(arr, key=lambda x:x[1])

print(arr)
