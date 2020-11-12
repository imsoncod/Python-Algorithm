n,m = map(int, input().split())
card = []
answer = 0
for _ in range(n):
    card.append(list(map(int, input().split())))
    answer = max(answer, min(card[-1]))

print(answer)
