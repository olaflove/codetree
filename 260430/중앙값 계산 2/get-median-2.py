n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr2 = []
arr3 = []
for i in range(n):
    arr2.append(arr[i])
    if i % 2 == 0:
        arr2.sort()
        ans = arr2[i//2]
        arr3.append(ans)

print(*arr3)