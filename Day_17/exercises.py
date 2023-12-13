class User:
    #pass
    # use pass to leave an empty class or function, if a class you can build the class straight from inputs like:
        # user_3 = User()
        # user_3.id = "003"
        #user_3.username = "bill

#this will make the attributes for the class
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
#this will make a method for the class
    def follow(self, user):
        user.followers += 1
        self.following += 1




user_1 = User("001", "angela")
user_2 = User("002", "jack")


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)