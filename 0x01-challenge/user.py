#!/usr/bin/python3
""" User class """
class User:
    """ Defines a user """
    def __init__(self):
        """ Initializes a User object """
        self.__email = None

    @property
    def email(self):
        """ Retrieves the email of a User instance """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets the email of a User instance """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
