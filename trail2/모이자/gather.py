n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
distances = []
for i in range(n):
    total = 0
    for j in range(n):
        total += A[j]*abs(j-i)

    distances.append(total)

print(min(distances))