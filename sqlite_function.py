import sqlite3

db = sqlite3.connect("sqlite_table.sqlite")
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


def insert(data, id):
    cur.execute(f"INSERT INTO {connection[id]} VALUES ('{data}')")
    db.commit()


def delete(id):
    cur.execute(f"DELETE FROM {connection[id]}")
    db.commit()


def select(id):
    cur.execute(f"SELECT * FROM {connection[id]}")
    return cur.fetchall()
