from datetime import datetime


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
        print('Заметка отредактирована')
    except TypeError:
        print('\nЗапись отсутствует')

# удаление заметки
def delete_note(notes, index):
    try:
        del notes[index]
        print('Заметка удалена')
    except TypeError:
        print('\nЗапись отсутствует')

def get_index(notes, text):
    length_notes = get_length_notes(notes)
    try:
        if len(notes) == 0:
            return
        index = int(input(f'Введите номер заметки, которую хотите {text}: ')) - 1
        if -1 < index < length_notes:
            return index
    except Exception:
        print('⚠ Ошибка исполнения. Нужен номер записи. ⚠')

def get_length_notes(notes):
    # получение количества записей
    length_notes = len(notes)
    return length_notes