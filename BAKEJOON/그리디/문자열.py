#a의 길이는 b의 길이보다 작거나 같다
a, b = input().split()
index = len(b)-len(a)
ans = 50

#a를 한칸씩 뒤로 미루면서 b와 비교
#앞,뒤에 추가 될 알파벳은 a와b가 서로 같게끔 아무거나 추가하면 되므로 신경쓰지 않아도됨
for i in range(index+1):
    temp = 0
    for j in range(i, i+len(a)):
        if a[j-i] != b[j]:
            temp += 1
    ans = min(ans, temp)
print(ans)
