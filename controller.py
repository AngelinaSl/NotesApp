from datetime import timedelta, datetime

from data_base import load_notes, save_notes
from funcs import add_note, edit_note, delete_note, filter_notes, get_index, get_datatime
from view import list_notes, show_note, menu_printing
from colorama import init, Fore

init()
def notesApp():
    file = 'notes.json'
    notes_param = load_notes(file)
    while True:
        menu_printing()
        cmd = input('\nВыберите команду: ')
        match cmd:
            case '1':
                notes_param.append(add_note())
                save_notes(file, notes_param)
                print(Fore.GREEN + '✔ Заметка добавлена ✔' + '\033[39m')
            case '2':
                list_notes(notes_param)
            case '3':
                index = get_index(notes_param, 'открыть')
                show_note(notes_param, index)
            case '4':
                index = get_index(notes_param, 'редактировать')
                edit_note(notes_param, index)
                save_notes(file, notes_param)
            case '5':
                index = get_index(notes_param, 'удалить')
                delete_note(notes_param, index)
                save_notes(file, notes_param)
            case '6':
                if notes_param:
                    start_date = get_datatime('Начальная дата для поиска:')
                    end_date = get_datatime('Конечная дата для поиска (+1 день):')
                    filtered_notes = filter_notes(notes_param, start_date, end_date)
                    list_notes(filtered_notes)
                else:
                    print('Список заметок пуст')
            case '7':
                break
            case _:
                print(Fore.RED + 'Введите корректную команду' + '\033[39m')

