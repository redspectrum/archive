'''
Файл запускается через english.py

Пример что записано в базе:
users = [
    ["interrupt",'прерывание'],
    ["generically", 'обобщенно'],
    ["bob", 'боб']
]
'''

import pickle
import random


# Добавление слова в базу
def add_new_data_word(filename, en_word, ru_word):
    users2 = []
    user3 = []

    user3.append(en_word)
    user3.append(ru_word)
    users2.append(user3)

    with open(filename, "rb") as file:
        users_from_file = pickle.load(file)

    with open(filename, "wb") as file2:
        pickle.dump(users_from_file + users2, file2)


# Печать базы
def print_data_words(filename):
    with open(filename, "rb") as file:
        users_from_file = pickle.load(file)

    for user in users_from_file:
        print("English:", user[0], "\tRussian:", user[1])


# удаление слова из базы
def del_data_word(filename, del_word):
    with open(filename, "rb") as file:
        users_from_file = pickle.load(file)

    # удаление
    for i in range(len(users_from_file)):
        if users_from_file[i][0] == del_word:
            del users_from_file[i]
            with open(filename, "wb") as file2:
                pickle.dump(users_from_file, file2)


def random_word(filename):
    with open(filename, "rb") as file:
        users_from_file = pickle.load(file)

    return (users_from_file[random.randint(0, len(users_from_file) - 1)])


if __name__ == "__main__":
    del_data_word("users.dat", 'hru')
    print(random_word("users.dat"))
    print_data_words("users.dat")
