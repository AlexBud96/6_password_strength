import os
import re
from blacklist import list

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    file = open(filepath, "r")
    text = file.read()
    file.close()
    return text
    
def blacklist_inspection(password):
    for string in list:
        if password.find(string) != -1:
            print('Ваш пароль содержит слово из списка недопустимых паролей.')
            return 0
    return 1

def case_sensitivity(password):
    if not password.islower() and not password.isupper():
        return 2
    else:
        return 1
        
def numerical_digits(password):
    if password.isdigit():
        print("Invalid password(only numerical digits)")
        return 1
    else:
        for char in password:
            if char.isdigit():
                return 2
        return 0
        
def special_characters(password):
    if re.search('\W', password):
        return 2
    return 1
    
def whitespace_characters(password):
    if re.search('\s', password):
        print('Invalid password(whitespace characters)')
        return 0
    else: 
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
    strength = 0
    strength += blacklist_inspection(password)
    strength += case_sensitivity(password)
    strength += numerical_digits(password)
    strength += special_characters(password)
    strength += password_length(password)
    return strength


if __name__ == '__main__':
    password = input('Введите пароль: ')
    if whitespace_characters(password):
        str = get_password_strength(password)
        print('Ваш пароль набрал %d баллов из 10' % (str))
