from tkinter import *
from PIL import ImageTk, Image
import pickle
import data_words


# Кнопка добавления новой записи
def command_but1():
    modal = Tk()
    modal.title('Добавление новой записи')
    modal.minsize(310, 180)

    lab = Label(modal, text='Добавьте новое слово!', font="Arial 18").grid(row=1, column=1)
    l = Label(modal, text='English')
    l.grid(row=3, column=1)
    l1 = Label(modal, text='Russian')
    l1.grid(row=3, column=2)

    a = Entry(modal, width=25)
    a.grid(row=2, column=1)

    a1 = Entry(modal, width=25)
    a1.grid(row=2, column=2)

    # Кнопка Сохранить и ее функция
    def save():
        data_words.add_new_data_word("users.dat", a.get(), a1.get())

        modal2 = Tk()
        modal2.title('Добавление новой записи')
        modal.minsize(300, 220)
        l = Label(modal2, text='Новое слово добавлено!', font="Arial 18")
        l.grid(row=1, column=1)

        def save_ok():
            modal2.destroy()
            modal.destroy()

        button_save = Button(modal2, text='Ок', bg='white', fg='black', font='Arial', width=15, height=1,
                             command=save_ok).grid(row=3, column=2)

    button_save = Button(modal, text='Сохранить', bg='white', fg='black', font='Arial', width=15, height=1,
                         command=save).grid(row=5, column=2)
    modal.mainloop()


# Кнопка 2 ЗАПУСК тренировки
def command_but2():
    modal_trainer = Tk()
    modal_trainer.title('Тренировка')
    modal_trainer.minsize(500, 200)
    modal_trainer.resizable(width=False, height=False)

    def new_word():
        # обращаемся к базе за словосочетанием  [0]-английский [1]-русский
        new_words = data_words.random_word("users.dat")

        lab = Label(modal_trainer, text=new_words[0], font="Arial 18")
        lab.grid(row=1, column=2)

        l = Label(modal_trainer, text='Введите слово на русском: ')
        l.grid(row=2, column=1)

        a1 = Entry(modal_trainer, width=25)
        a1.grid(row=2, column=2)
        a1.focus()

        # Кнопка ДАЛЕЕ
        def go_next(event=None):

            def go_next2(event=None):
                a1.destroy()
                lab.destroy()
                button_go_next2.destroy()
                button_delete.destroy()
                l.destroy()
                l1.destroy()
                new_word()

            button_go_next2 = Button(modal_trainer, text='Далее', bg='white', fg='black', font='Arial', width=15,
                                     height=1,
                                     command=go_next2)
            button_go_next2.grid(row=5, column=3)

            if a1.get() == new_words[1]:
                l = Label(modal_trainer, text='ВЕРНО!', font='Arial 18', fg='green')
                l.grid(row=5, column=2)
                l1 = Label(modal_trainer, text=new_words[1], font='Arial 18', fg='green')
                l1.grid(row=1, column=3)
            else:
                l = Label(modal_trainer, text='НЕ ВЕРНО!', font='Arial 18', fg='red')
                l.grid(row=5, column=2)
                l1 = Label(modal_trainer, text=new_words[1], font='Arial 18', fg='red')
                l1.grid(row=1, column=3)
            button_go_next.destroy()

            a1.bind('<Return>', go_next2)

        button_go_next = Button(modal_trainer, text='Далее', bg='white', fg='black', font='Arial', width=15, height=1,
                                command=go_next)
        button_go_next.grid(row=5, column=3)

        a1.bind('<Return>', go_next)

        def delete_off():
            # Удаляем на английском слово и словосочетание
            data_words.del_data_word("users.dat",
                                     new_words[0])
            # создание окна для удаления слова
            modal_stop = Tk()
            modal_stop.title('Удаление слова')
            modal_stop.minsize(300, 100)
            modal_stop.resizable(width=False, height=False)

            l = Label(modal_stop, text='Слово изучено и  удалено!', font="Arial 18")  # заголовок который мы видим
            l.grid(row=1, column=1)

            def save_ok():
                modal_stop.destroy()

            button_save = Button(modal_stop, text='Ок', bg='white', fg='black', font='Arial', width=10, height=1,
                                 command=save_ok).grid(row=3, column=1)

        button_delete = Button(modal_trainer, text='Удалить Слово', bg='white', fg='black', font='Arial', width=15,
                               height=1,
                               command=delete_off)
        button_delete.grid(row=5, column=1)

    # Кнопка Закончить Тренировку и ее функция
    def stop_trainer():
        modal_stop = Tk()
        modal_stop.title('Остановка')
        modal_stop.minsize(300, 100)
        modal_stop.resizable(width=False, height=False)

        l = Label(modal_stop, text='Тренировка закончена!', font="Arial 18")
        l.grid(row=1, column=1)

        def save_ok():
            modal_stop.destroy()
            modal_trainer.destroy()

        button_ok = Button(modal_stop, text='Ок', bg='white', fg='black', font='Arial', width=10, height=1,
                           command=save_ok).grid(row=3, column=1)

    button_stop_trainer = Button(modal_trainer, text='Закончить', bg='white', fg='black', font='Arial', width=15,
                                 height=1,
                                 command=stop_trainer).grid(row=6,
                                                            column=1)

    new_word()
    modal_trainer.mainloop()


def start_program():
    root = Tk()
    root.title('Тренировка слов')
    root.geometry('555x290')
    root.resizable(width=False, height=False)
    # создаем рабочую область
    frame = Frame(root)
    frame.grid()
    label = Label(frame, text="").grid(row=1, column=1)
    button_start = Button(frame, text='START', bg='white', fg='black', font='Arial', width=11, height=1,
                          command=command_but2).grid(row=2, column=1)
    button_add = Button(frame, text='Add new Word', bg='white', fg='black', font='Arial', width=11, height=1,
                        command=command_but1).grid(row=4, column=1)
    # вставка изображения
    canvas = Canvas(root, height=500, width=500)
    image = Image.open("english.png")
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(-10, -60, anchor='nw', image=photo)
    canvas.grid(row=1, column=1)
    root.mainloop()


if __name__ == '__main__':
    start_program()
