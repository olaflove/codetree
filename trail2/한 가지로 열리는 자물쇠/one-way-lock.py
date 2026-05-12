N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.

cnt = 0
for i in range(1, N+1):
    if abs(a-i) >= 3:
        for j in range(1, N+1):
            if abs(b-j) >= 3:
                 for k in range(1, N+1):
                    if abs(c-k) >= 3:
                        cnt += 1

ans = (N*N*N) - cnt

print(ans)