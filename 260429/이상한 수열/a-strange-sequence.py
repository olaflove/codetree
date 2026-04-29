N = int(input())

def num(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return num(n // 3) + num(n - 1)

print(num(N))
