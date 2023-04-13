import json


# загрузка заметок из БД в список
def load_notes(file):
    try:
        with open(file) as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes


# сохранение списка заметок в БД
def save_notes(file, notes):
    with open(file, 'w') as f:
        json.dump(notes, f)