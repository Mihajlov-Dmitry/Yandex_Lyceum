import sqlite3

db = sqlite3.connect("utils/sqlite_table.sqlite")
cur = db.cursor()

connection = {
    1: "basket",
    21: "now_1",
    22: "now_2",
    3: "expectation",
    4: "calendar",
    5: "projects",
    61: "then_1",
    62: "then_2",
    71: "notes_1",
    72: "notes_2",
    73: "notes_2"
}


def insert(data: str, id: int) -> None:
    """
    Сохранение данных в SQLite
    :param data: Переданные данные
    :param id: Индивидуальный номер виджета, от которого поступают данные
    :return: None
    """

    cur.execute(f"INSERT INTO {connection[id]} VALUES ('{data}')")
    db.commit()


def delete(id: int) -> None:
    """
    Удаление всей информации из таблицы SQLite
    :param id: Индивидуальный номер виджета, данные которого нужно удалить
    :return: None
    """

    cur.execute(f"DELETE FROM {connection[id]}")
    db.commit()


def select(id: int) -> list:
    """
    Считывание данных из SQLite
    :param id:  Индивидуальный номер виджета, для которого нужно получить данные
    :return: None
    """

    cur.execute(f"SELECT * FROM {connection[id]}")
    return cur.fetchall()
