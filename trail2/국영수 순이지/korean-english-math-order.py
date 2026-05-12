n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

idx = list(range(n))
idx.sort(key=lambda i: (-korean[i], -english[i], -math[i]))
for i in idx:
    print(name[i], korean[i], english[i], math[i])
