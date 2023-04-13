from textwrap import wrap
from colorama import init, Fore

init()


def menu_printing():
    print('\n▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾▾')
    print('   1  ┆  Добавить заметку')
    print('   2  ┆  Посмотреть список заметок')
    print('   3  ┆  Посмотреть заметку')
    print('   4  ┆  Редактировать заметку')
    print('   5  ┆  Удалить заметку')
    print('   6  ┆  Поиск заметок по дате')
    print('   7  ┆  Выход')
    print('▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴▴')


def decorator_table(func):
    def wrapper(*args, **kwargs):
        print('  ')
        table_print()
        func(*args, **kwargs)
        end_table_print()
    return wrapper


def table_print():
    print(f"╔{'═' * 3}╦{'═' * 22}╦{'═' * 21}╦{'═' * 62}╗")
    print(f"║ № ║ {'Заголовок':^20s} ║ {'Дата изменения':^19s} ║ {'Текст заметки':^60s} ║")
    print(f"╠{'═' * 3}╬{'═' * 22}╬{'═' * 21}╬{'═' * 62}╣")


def end_table_print():
    print(f"╚{'═' * 3}╩{'═' * 22}╩{'═' * 21}╩{'═' * 62}╝")


# вывод списка заметок на экран
@decorator_table
def list_notes(notes):
    if len(notes) == 0:
        print('Список заметок пуст. Добавьте заметку.')
    else:
        for i, note in enumerate(notes):
            print(f"║ {i + 1} ║ {note['title'][:20]:20s} ║ {note['date']} ║ {note['body'][:60]:60s} ║")


def show_note(notes, index):
    # вывод одной заметки
    try:
        note = notes[index]
        txt = note['body']
        print(Fore.YELLOW + '\n   ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆')
        print(f"\n{'Заголовок':<13s}: {note['title']}" )
        print(f"{'Дата изменения':<13s}: {note['date']}")
        # print(f"{'Текст заметки':<13s}: ")
        print(" ")
        line_break(txt)
        print('\n   ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆'+ '\033[39m')
    except TypeError:
        print(Fore.RED + '\n⚠ Запись отсутствует ⚠'+ '\033[39m')


def line_break(text):
    # печать текста заметки по строкам
    lines = wrap(text, width=120)
    x = 0
    while len(lines) > x:
        print(lines[x])
        x += 1



