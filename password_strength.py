import os
import re
import getpass
from blacklist import blacklist
        

def get_user_password():
    password = getpass.getpass('Введите пароль: ')
    return password


def check_password_conformity(password):
    for string in blacklist:
        if (string in password):
            print('Ваш пароль содержит слово из списка недопустимых паролей.')
            return 0
    if password.isdigit():
        print("Invalid password(only numerical digits)")
        return 0
    if re.search('\s', password):
        print('Invalid password(whitespace characters)')
        return 0
    else: 
        return 1


    
def blacklist_inspection(password):
    
    return 1

def case_sensitivity(password):
    if not password.islower() and not password.isupper():
        return 2
    else:
        return 1
        
def numerical_digits(password):
    for char in password:
        if char.isdigit():
            return 1
    return 0
        
def special_characters(password):
    if re.search('\W', password):
        return 1
    return 1
      
    
def password_length(password):
    if len(password)<8:
        return 1
    else:
        if len(password)<12:
            return 2
        else:
            return 3
            


def get_password_strength(password):
    minimal_password_strength = 3       # минимальная оценка после проверки в функции check_password_conformity
    strength = minimal_password_strength
    strength += case_sensitivity(password)
    strength += numerical_digits(password)
    strength += special_characters(password)
    strength += password_length(password)
    return strength


if __name__ == '__main__':
    password = get_user_password()
    if check_password_conformity(password):
        strength = get_password_strength(password)
        print('Ваш пароль набрал %d баллов из 10' % (strength))
