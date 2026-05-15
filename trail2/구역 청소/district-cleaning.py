a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
checked = [0] * 101

for i in range(a, b):
    checked[i] = 1

for i in range(c, d):
    checked[i] = 1

print(sum(checked))