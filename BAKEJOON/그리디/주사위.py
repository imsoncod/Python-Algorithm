n = int(input())
dice = list(map(int, input().split()))

temp = sorted([min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])])

print(temp)

cnt_three = 4
cnt_two = 8*(n-2) + 4
cnt_one = 5*(n-2)*(n-2) + 4*(n-2)

sum_three = sum(temp[:3])
sum_two = sum(temp[:2])
sum_one = sum(temp[:1])

ans = sum(sorted(dice)[:5]) if n == 1 else cnt_three*sum_three + cnt_two*sum_two + cnt_one*sum_one

print(ans)
