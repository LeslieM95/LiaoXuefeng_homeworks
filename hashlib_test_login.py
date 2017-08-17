#!/usr/bin/env/Python
# - * - coding: utf-8 - * -


import hashlib


def get_md5(password, user):  # user为salt
    md5 = hashlib.md5()
    md5.update((password + user).encode('utf-8'))
    return md5.hexdigest()


def calc_md5(password):  # 这样定义两个函数，可以在定义calc_md5()时没有user参数
    return get_md5(password, user1)  # 但，内部的get_md5()却可以引用user1参数(user1为__main__中的input变量)


db = {
    'michael': 'ab281e4aedd3e9981074f8f4c380eb3e',
    'bob': '2071ea452154a0d74bc3c77f032ff27a',
    'alice': 'b430935d83cbe1e08e46fa2235164a98'
}


def login(user, password):
    if calc_md5(password) == db[user]:
        print('True')
        return True
    else:
        print('False')
        return False


def register(user, password):
    if user in db:
        print('This username has already existed')
    else:
        db[user] = calc_md5(password)
        print('Register done! You can login now!')


if __name__ == '__main__':
    for i in range(1, 4):

        while True:
            user1 = input('Please input your user name:')
            password = input('Please input your password:')

            if user1 not in db:
                print('Please register first!')
                user1 = input('Please input your user name:')
                password = input('Please input your password:')

                register(user1, password)
            else:
                break

        if login(user1, password) is False:
            if i != 3:
                print('You have %s chance(s)' % (3-i))
            else:
                print('You have no chance!')
        else:
            break

