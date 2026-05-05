s = input()

open_cnt = 0
answer = 0

for ch in s:
    if ch == '(':
        open_cnt += 1
    else:
        answer += open_cnt

print(answer)