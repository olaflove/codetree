secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Secret:
    def __init__(self, s, m, t):
        self.s = s
        self.m = m
        self.t = t

person1 = Secret(secret_code, meeting_point, time)
print("secret code :", person1.s)
print("meeting point :", person1.m)
print("time :", person1.t)