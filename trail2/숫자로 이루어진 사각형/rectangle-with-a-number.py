n = int(input())

# Please write your code here.

def square(m):
    num = 1

    for _ in range(m):
        for _ in range(m):
            print(num, end=' ')
            
            num += 1
            if num == 10:
                num = 1

        print()

square(n)

