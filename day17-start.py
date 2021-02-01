class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f"created new user with id: {id} and username: {username}")

    def new_follow(self, user):
        self.followers += 1
        self.following += 1

user_1 = User('001', 'jd')
user_2 = User('002', 'juan')

user_1.new_follow(user_2)
print(user_1.following)
