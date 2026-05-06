N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
ans = 0
for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if A[a] <= A[b] <= A[c]:
                ans += 1

print(ans)