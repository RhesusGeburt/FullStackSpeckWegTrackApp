import sqlite3


def initialize():
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            age INTEGER,
            height INTEGER
        );
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS weights(
            id INTEGER PRIMARY KEY,
            user INTEGER NOT NULL,
            weight REAL NOT NULL,
            date TEXT NOT NULL
        );
        """
    )
    connection.commit()
    connection.close()


def add_weight(user, weight, date):
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO weights (user, weight, date) VALUES (?, ?, ?)",
        (user, weight, date),
    )
    connection.commit()


def add_user(name, password):
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, password) VALUES (?, ?)",
        (name, password),
    )
    connection.commit()


def set_age(id, age):
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET age = (?) WHERE id = (?)",
        (age, id),
    )
    connection.commit()


def set_height(id, height):
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET height = (?) WHERE id = (?)",
        (height, id),
    )
    connection.commit()


def get_id(name):
    connection = sqlite3.connect("speckweg.db")
    rows = connection.execute(
        "SELECT id FROM users WHERE name LIKE (?)", (name,)).fetchall()
    return rows


def get_users():
    connection = sqlite3.connect("speckweg.db")
    users = connection.execute(
        "SELECT name FROM users").fetchall()
    return users


def get_history(user):
    connection = sqlite3.connect("speckweg.db")
    history = connection.execute(
        "SELECT weight, date FROM weights WHERE user = (?) ORDER BY date",
        (user,),).fetchall()
    return history


def reset_db():
    connection = sqlite3.connect("speckweg.db")

    connection.execute("DROP TABLE IF EXISTS users")
    connection.execute("DROP TABLE IF EXISTS weights")

    connection.commit()
    connection.close()

    initialize()
