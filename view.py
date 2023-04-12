from textwrap import wrap


def decorator_table(func):
    def wrapper(*args, **kwargs):
        table_print()
        table_print_header()
        table_print()
        func(*args, **kwargs)
        table_print()
    return wrapper


def table_print():
    # footer таблицы
    print(f"+{'-' * 3}+{'-' * 22}+{'-' * 21}+{'-' * 62}+")




def table_print_header():
    # header таблицы
    print(f"| № | {'Заголовок':^20s} | {'Дата изменения':^19s} | {'Текст заметки':^60s} |")


@decorator_table
def list_notes(notes):
    # вывод списка заметок на экран
    if len(notes) == 0:
        print('Список заметок пуст')
    else:
        for i, note in enumerate(notes):
            print(f"| {i + 1} | {note['title'][:20]:20s} | {note['date']} | {note['body'][:60]:60s} |")


def show_note(notes, index):
    # вывод одной заметки
    try:
        note = notes[index]
        txt = note['body']
        print(f"\n{'Заголовок':<13s}: {note['title']}")
        print(f"{'Дата изменения':<13s}: {note['date']}")
        print(f"{'Текст заметки':<13s}: ")
        line_break(txt)
    except TypeError:
        print('\nЗапись отсутствует')


def line_break(text):
    # печать текста заметки по строкам
    lines = wrap(text, width=120)
    x = 0
    while len(lines) > x:
        print(lines[x])
        x += 1


def menu_printing():
    # вывод меню команд
    print('\n1 - Посмотреть все заметки')
    print('2 - Добавить заметку')
    print('3 - Редактировать заметку')
    print('4 - Удалить заметку')
    print('5 - Просмотр заметки')
    print('6 - Поиск заметок по дате')
    print('7 - Выход')