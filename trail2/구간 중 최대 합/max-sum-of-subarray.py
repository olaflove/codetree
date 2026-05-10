n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_v = 0
for i in range(n-k+1):
    ans = 0
    for j in range(i, i+k):
        ans += arr[j]

    max_v = max(ans, max_v)

print(max_v)