from hashlib import sha256
import json
import os

from FileManager import FileManager
from config import USER_STORAGE


commands = {
    '0': 'Вывести текущую директорию',
    '1': 'Создать папку',
    '2': 'Удалить папку',
    '3': 'Перемещение между папками',
    '4': 'Создать пустой файл',
    '5': 'Записать текст в файл',
    '6': 'Просмотреть содержимое текстового файла',
    '7': 'Удалить файл',
    '8': 'Копировать файл из одной папки в другую',
    '9': 'Переместить файл',
    '10': 'Переименовать файл',
    'menu': 'Вывести это меню',
    'exit': 'Выйти из программы',
}


def hash_passwd(password):
    return sha256(bytes(password, 'utf-8')).hexdigest()


def validate_passwd(password, hashed):
    return hash_passwd(password) == hashed


def append_user_to_file(data, login, hashed):
    with open('storage/users.json', 'w') as f:
        data.update({login: str(hashed)})
        print(data)
        f.seek(0)
        json.dump(data, f)


def print_menu():
    for k,v in commands.items():
        print(f"{k}. {v}")


def login_register():
    with open('storage/users.json',) as file:
        users = json.load(file)
    while True:
        username = str(input('Введите ваш логин: '))
        if not users.get(username) is None:
            password = str(input('Введите ваш пароль: '))
            hashed = users.get(username)
            if validate_passwd(password, hashed):
                print('Вы успешно авторизовались')
                return True, username
            else:
                print('Неправильный пароль')
                return False, None
        else:
            password = str(input('Вы не зарегистрированы. Введите пароль: '))
            hashed = hash_passwd(password)
            append_user_to_file(users, username, hashed)
            print('Регистрация прошла успешно. Продолжайте работу')
            return True, username


def auth():
    for i in range(1,4):
        if i > 1:
            print(f'Попытка авторизации номер {i}')
        resp = login_register()
        if resp[0]:
            return resp
    return False, None


def run():
    authenticate = auth()
    if authenticate[0]:
        print(f'Инициализируем файловый менеджер в папке {authenticate[1]} ...')
        fm = FileManager(USER_STORAGE, authenticate[1])
        print_menu()
        command = ''
        while command != 'exit':
            command = input('введите номер команды: ')
            if command == 'menu':
                print_menu()
            elif command == 'exit':
                break
            else:
                fm.execute_command(command)
    else:
        print('Неудачная авторизация')


if __name__ == '__main__':
    run()