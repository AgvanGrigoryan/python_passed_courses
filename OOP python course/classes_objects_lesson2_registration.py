import re
import string

class User:
    """BLAAAAA BLAAAA BLA ahhaha"""
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self,value):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, value):
            self.__login = value
        else:
            raise ValueError("Invalid Email address,email must contain '@', '.' sign")

    
    @property
    def password(self):
        print("getter called")
        return self.__password

    @staticmethod
    def contain_digit(password):
        for digit in string.digits:
            if digit in password:
                return True
        return False
    
    @staticmethod
    def is_include_only_latin(password):
        for d in password:
            if d not in string.printable:
                return False
        return True
    
    @staticmethod
    def is_include_all_register(password):
        count={"UPPER_CASE": 0, "LOWER_CASE": 0}
        for d in password:
            if count['UPPER_CASE']>=2 and count['LOWER_CASE']>0:
                return True
            if d.isupper():
                count['UPPER_CASE']+=1     
            elif d.islower():
                count['LOWER_CASE']+=1
            else:
                pass
        return False
    
    @staticmethod
    def is_easy_password(password):
        with open(file='easy_passwords.txt', encoding='utf-8') as file:
            for word in file.readlines():
                if password == word.strip():
                    return True
            return False

    @staticmethod
    def password_validate(password):
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        if len(password)<4:
            raise ValueError("Password length is too short, must be greathen than 4 symbols")
        if len(password)>12:
            raise ValueError("Password length is too long, must be less than 12 symbols")
        if not User.contain_digit(password):
            raise ValueError("Password must contain at least one digit")
        if not User.is_include_only_latin(password):
            raise ValueError("Password must contain only latin aplhabet")
        if not User.is_include_all_register(password):
            raise ValueError("Password must contain at least 2 Upper and 1 lower  Case letters")
        if User.is_easy_password(password):
            raise ValueError("Your password is a common password, try to make it more difficult")


        
    @password.setter
    def password(self, value):
        print("setter called")
        User.password_validate(value)
        self.__password = value
