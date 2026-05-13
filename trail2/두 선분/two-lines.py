x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.

if x4 < x1 or x2 < x3:
    print('nonintersecting')
else:
    print('intersecting')