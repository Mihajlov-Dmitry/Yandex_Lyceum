import sqlite3

db = sqlite3.connect("sqlite_table.sqlite")
cur = db.cursor()

connection = {
    1: "basket",
    21: "now_1",
    22: "now_2",
    4: "calendar"
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


