from datetime import datetime
from colorama import init, Fore

init()


# добавление заметки
def add_note():
    title = input('Название: ')
    body = input('Текст заметки: ')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {'title': title, 'body': body, 'date': date}


# редактирование заметки
def edit_note(notes, index):
    try:
        note = notes[index]
        title = input(f'Новый заголовок ({note["title"]}): ')
        body = input(f'Новый текст ({note["body"]}): ')
        if title:
            note['title'] = title
        if body:
            note['body'] = body
        note['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(Fore.GREEN + '✓ Заметка отредактирована ✓' + '\033[39m')
    except TypeError:
        print(Fore.RED + '\n⚠ Запись отсутствует ⚠' + '\033[39m')


# удаление заметки
def delete_note(notes, index):
    try:
        del notes[index]
        print(Fore.GREEN + 'Заметка удалена' + '\033[39m')
    except TypeError:
        print(Fore.RED + '\n⚠ Запись отсутствует ⚠' + '\033[39m')


def get_index(notes, text):
    length_notes = get_length_notes(notes)
    try:
        if len(notes) == 0:
            return
        # index = int(input(f'Номер заметки для {text} от 1 до {length_notes}: ')) - 1
        index = int(input(f'Введите номер заметки, которую хотите {text}: ')) - 1
        if -1 < index < length_notes:
            return index
    except Exception:
        print(Fore.RED + '⚠ Ошибка исполнения. Нужен номер записи. ⚠'+ '\033[39m')


def get_length_notes(notes):
    # получение количества записей
    length_notes = len(notes)
    return length_notes


def filter_notes(notes, start_date, end_date):
    # фильтрация заметок по дате
    filtered_notes = list(filter(lambda note: start_date <= note['date'] <= end_date, notes))
    return filtered_notes

def get_value(text_value):
    while True:
        try:
            value = abs(int(input(f'Введите {text_value} для поиска: ')))
            return value
        except Exception:
            print(Fore.RED + '⚠ Ошибка даты ⚠'+ '\033[39m')
def get_datatime(text):
    print(text)
    while True:
        while True:
            year = str(get_value('год'))
            match len(year):
                case 1:
                    date_str = '200' + year + ' '
                    break
                case 2:
                    date_str = '20' + year + ' '
                    break
                case 3:
                    date_str = '0' + year + ' '
                    break
                case 4:
                    date_str = year + ' '
                    break
                case _:
                    print(Fore.RED + '⚠ Ошибка в значении ⚠' + '\033[39m')
        while True:
            month = get_value('месяц')
            if 1 <= month <= 12:
                date_str += str(month) + ' '
                break
            else:
                print(Fore.RED + '⚠ Ошибка в значении ⚠' + '\033[39m')
        while True:
            day = get_value('день')
            match month:
                case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                    if 1 <= day <= 31:
                        date_str += str(day)
                        break
                case 4 | 6 | 9 | 11:
                    if 1 <= day <= 30:
                        date_str += str(day)
                        break
                case 2:
                    if int(date_str[:4]) % 4 == 0:
                        if 1 <= day <= 29:
                            date_str += str(day)
                            break
                    elif 1 <= day <= 28:
                        date_str += str(day)
                        break
                    else:
                        print(Fore.RED + '⚠ Ошибка в значении ⚠' + '\033[39m')
        start_date = datetime.strptime(date_str, '%Y %m %d').strftime('%Y-%m-%d')
        print(f'Дата для поиска: {start_date}')
        push = input('Дата верна (Д/Н): ')
        if push.lower() == 'y' or push.lower() == 'д' or push.lower() == '':
            return start_date


