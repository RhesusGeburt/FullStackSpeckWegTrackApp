import sqlite3


def initialize():
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            height INTEGER NOT NULL
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS weights(
            id INTEGER PRIMARY KEY,
            weight INTEGER NOT NULL,
            date TEXT NOT NULL
        );
        """
    )


def add_weight(id, weight, date):
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO weights (id, weight, date) VALUES (?, ?, ?)",
        (id, weight, date),
    )
    connection.commit()


def add_user(name, age, height):
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, age, height) VALUES (?, ?, ?)",
        (name, age, height),
    )
    connection.commit()


def get_id(name):
    connection = sqlite3.connect("speckweg.db")
    rows = connection.execute(
        "SELECT id FROM users WHERE name LIKE (?)", (name,)).fetchall()
    return rows


def get_history(id):
    connection = sqlite3.connect("speckweg.db")
    history = connection.execute(
        "SELECT weight, date FROM weights WHERE id = (?) ORDER BY date",
        (id,),).fetchall()
    return history


def reset_db():
    connection = sqlite3.connect("speckweg.db")
    rows = connection.execute("DROP TABLE users")
    rows = connection.execute("DROP TABLE weights")
    initialize()
