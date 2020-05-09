# 1
s = input()
w = input()
print(s.count(w))

# 2
cnt = 0
idx = 0
while idx < len(s):
    if w == s[idx:idx+len(w)]:
        cnt+=1
        idx += len(w)
    else:
        idx += 1
print(cnt)
