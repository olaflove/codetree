n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str.sort()
cnt = 0
for s in str:
    if s.startswith(t):
        cnt += 1
        if cnt == k:
            print(s)