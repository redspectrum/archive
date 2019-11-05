from tkinter import *
import time
import vk
import random
import re
import requests
import pickle
import threading


# ========================Вход=======================================

def command_start():
    modal_trainer = Tk()
    modal_trainer.title('Вход в программу')
    modal_trainer.minsize(280, 120)
    modal_trainer.resizable(width=False, height=False)

    # Вход в программу ЛОГИН
    login_entry = Entry(modal_trainer, width=25)
    login_entry.place(x=70, y=10)
    l = Label(modal_trainer, text='login')
    l.place(x=10, y=10)

    # Вход в программу ПАРОЛЬ
    pass_entry = Entry(modal_trainer, width=25, show='*')
    pass_entry.place(x=70, y=30)
    l1 = Label(modal_trainer, text='password')
    l1.place(x=10, y=30)

    # Окно ошибки при неправильном некорректном вводе логина и пароля
    def error_entry():
        modal_stop = Tk()
        modal_stop.title('Вход')
        modal_stop.minsize(300, 100)
        modal_stop.resizable(width=False, height=False)

        l = Label(modal_stop, text='Введите корректные данные', font="Arial 18")
        l.grid(row=1, column=1)

        def save_ok():
            modal_stop.destroy()

        button_ok = Button(modal_stop, text='Ок', bg='white', fg='black', font='Arial', width=10, height=1,
                           command=save_ok).grid(row=3, column=1)

    # кнопка Войти
    def stop_trainer():
        # Проверяем введен ли логин и пароль
        if login_entry.get() and pass_entry.get():
            # Проверка
            if (re.findall(pass_entry.get(), requests.get('http://onlinero.github.io').text)):
                modal_trainer.destroy()
                main_start()
            else:
                error_entry()
        else:
            error_entry()

    button_stop_trainer = Button(modal_trainer, text='Вход', bg='white', fg='black', font='Arial', width=15, height=1,
                                 command=stop_trainer)
    button_stop_trainer.place(x=60, y=70)
    modal_trainer.mainloop()


# ========================Начало программы=======================================
def main_start():
    def vk_repost(id_user):
        session = vk.AuthSession(app_id=app_entry.get(), user_login=login_entry.get(),
                                 user_password=pass_entry.get(), scope='wall')
        # https://vk.com/id280795206?w=wall280795206_126

        vkapi = vk.API(session)
        WALL = vkapi.wall.get(owner_id=id_user, count=5)
        # print(WALL[1]['id'])
        #  Получаем id записи на стене
        try:
            WALL_ID = 'wall' + id_user + '_' + str(
                WALL[random.randint(1, 5)]['id'])
            # получаем ссылку wall280795206_126 одной записи из 5 последних
            vkapi.wall.repost(object=WALL_ID)
            output_log.insert(END, '\nГотово')
        except Exception:
            print('Нельзя репостнуть')
            output_log.insert(END, '\nНельзя репостнуть')

    def start_repost():
        if login_entry.get() and pass_entry.get() and app_entry.get():
            print('Выполнение программы')
            output_log.insert(END, '\nВыполнение программы')

            # Проверка типа id записи
            list = output.get(1.0, END).split()
            for i in range(len(list)):
                if (list[i][0:17]) == 'https://vk.com/id':
                    id_user = list[i][17:]
                elif (list[i][0:2]) == 'id':
                    id_user = list[i][2:]
                else:
                    id_user = list[i]
                print('user id = ' + id_user)
                output_log.insert(END, '\nДелаю репост id' + id_user)
                time.sleep(int(sleep_entry.get()))
                vk_repost(id_user)
                # Проверка последней записи и вывод окончание работы
                if i == len(list) - 1:
                    print('Все id обработаны')
                    output_log.insert(END, '\nВсе id обработаны')
                time.sleep(int(sleep_entry.get()))
        else:
            print('Введите корректные данные')
            output_log.insert(END, '\nВведите корректные данные')

    def auto_past():
        with open('users.dat', "rb") as file:
            users_from_file = pickle.load(file)
            print(users_from_file)

            if users_from_file:
                print('Данные заполнены')
                output_log.insert(END, '\nДанные заполнены')
                login_entry.delete(0, END)
                pass_entry.delete(0, END)
                app_entry.delete(0, END)
                login_entry.insert('0', users_from_file[0][0])
                pass_entry.insert('0', users_from_file[0][1])
                app_entry.insert('0', users_from_file[0][2])

    def auto_safe():
        if login_entry.get() and pass_entry.get() and app_entry.get():
            print('Данные сохранены')
            output_log.insert(END, '\nДанные сохранены')
            users2 = []
            user3 = []
            user3.append(login_entry.get())
            user3.append(pass_entry.get())
            user3.append(app_entry.get())
            users2.append(user3)

            with open('users.dat', "wb+") as file2:
                pickle.dump(users2, file2)
        else:
            modal_stop = Tk()
            modal_stop.title('Вход')
            modal_stop.minsize(300, 100)
            modal_stop.resizable(width=False, height=False)

            l = Label(modal_stop, text='Введите корректные данные', font="Arial 18")
            l.grid(row=1, column=1)

            def save_ok():
                modal_stop.destroy()

            button_ok = Button(modal_stop, text='Ок', bg='white', fg='black', font='Arial', width=10, height=1,
                               command=save_ok).grid(row=3, column=1)

    root_admin = Tk()
    root_admin.title('Subscribe')
    root_admin.minsize(680, 330)
    root_admin.resizable(width=False, height=False)

    # создаем текстовое окошко для вывода логов
    output_log = Text(root_admin, bg='white', font='Arial 12')
    output_log.place(x=160, y=115, width=500, height=200)

    scrol_log = Scrollbar(root_admin, command=output_log.yview)
    output_log.configure(yscrollcommand=scrol_log.set)
    scrol_log.place(x=660, y=180)

    # создаем текстовое окошко для ввода id
    output = Text(root_admin, bg='white', font='Arial 12')
    output.place(x=20, y=115, width=138, height=200)
    output.insert('0.0', '3670424\nid235899037\n3935541')

    scr = Scrollbar(root_admin, command=output.yview)
    output.configure(yscrollcommand=scr.set)
    scr.place(x=2, y=180)
    # поля ввода пароль логин апп
    login_entry = Entry(root_admin, width=25)
    login_entry.place(x=75, y=10)
    l = Label(root_admin, text='login')
    l.place(x=15, y=10)

    pass_entry = Entry(root_admin, width=25, show='*')
    pass_entry.place(x=75, y=30)
    l1 = Label(root_admin, text='password')
    l1.place(x=15, y=30)

    app_entry = Entry(root_admin, width=25)
    app_entry.place(x=75, y=50)
    l2 = Label(root_admin, text='app ID')
    l2.place(x=15, y=50)

    sleep_entry = Entry(root_admin, width=25)
    sleep_entry.place(x=75, y=90)
    sleep_entry.insert(0, '10')
    l3 = Label(root_admin, text='time sleep')
    l3.place(x=15, y=90)

    name_but1 = 'START'
    but1 = Button(root_admin, text=name_but1, width=8, height=2, fg='red', font='arial 14',
                  command=lambda: threading.Thread(target=start_repost).start())
    but1.place(x=560, y=50)

    but2 = Button(root_admin, text='Сохранить данные', command=auto_safe)
    but2.place(x=350, y=10)

    but3 = Button(root_admin, text='Вставить данные', command=auto_past)
    but3.place(x=240, y=10)

    root_admin.mainloop()


if __name__ == '__main__':
    command_start()
