unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second


bomb1 = Bomb(unlock_code, wire_color, seconds)
print("code :", bomb1.code)
print("color :", bomb1.color)
print("second :", bomb1.second)