n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
ans = []
for i in range(n):
    ans.append(nums[i]+nums[2*n-i-1])

print(max(ans))