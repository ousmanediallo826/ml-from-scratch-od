# 4. User Profile With Properties
#
# Create a UserProfile class.
#
# Practice:
#
# public attributes where appropriate
# private-style attribute _email
# property getter and setter for email
# validate email contains "@"
# static method: check strong password
# class method: create user from signup form dictionary
#
# Challenge: avoid generic get_email() and set_email() unless necessary.


class UserProfile:
    def __init__(self, email, name, password):
        self.__email = email
        self.name = name
        self.password = password


    @property
    def get_email(self):
        return self.__email
    @property
    def set_email(self):
        return self.__email
    def validate_email(self):
        if "@" not in self.__email:
            return "This email is not valid"
    @staticmethod
    def validate_password(password):
        if password == "":
            return "This password is empty"
        elif len(password) < 8:
            return "This password is too short"
        elif len(password) > 16:
            return "This password is too long"
        else:
            return "This password is strong"

    def user_login(self):
        userProfile = {
            "name": self.name,
            "email": self.__email,
            "password": self.password
        }
        for key, value in userProfile.items():
            print(f"the name of the user ")





user1 = UserProfile("Ousmane@speakhire.org", "Ousmane", "Talha826$")
print(user1.validate_email)
print(user1.validate_password)
print(user1.get_email)
print(user1.user_login())
user2 = UserProfile("ousmanediallo", "Ousmane", "Talha826$")
print(user2.validate_email)
print(user2.validate_password)
print(user2.get_email)
print(user2.user_login())

