class User:
    def __init__(self, id, name):
        print("new user...")
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

user1 = User("001", "howie")
user2 = User("002", "jack")

user2.follow(user1)

