user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Game:
    def __init__(self, id, lv):
        self.id = id
        self.lv = lv

user1 = Game("codetree", 10)
user2 = Game(user2_id, user2_level)

print("user", user1.id, "lv", user1.lv)
print("user", user2.id, "lv", user2.lv)