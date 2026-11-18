import sqlite3


def initialize():
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
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
    with sqlite3.connect("speckweg.db") as connection:
        connection.execute(
            "INSERT INTO weights (user, weight, date) VALUES (?, ?, ?)",
            (user, weight, date)
        )


def add_user(name):
    with sqlite3.connect("speckweg.db") as connection:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO users (name) VALUES (?)",
            (name),
        )


def add_user(name, password):
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, password) VALUES (?, ?)",
        (name, password),
    )
    connection.commit()


def set_age(id, age):
    with sqlite3.connect("speckweg.db") as connection:
        connection.execute(
            "UPDATE users SET age = ? WHERE id = ?",
            (age, id)
        )


def set_height(id, height):
    with sqlite3.connect("speckweg.db") as connection:
        connection.execute(
            "UPDATE users SET height = ? WHERE id = ?",
            (height, id)
        )


def get_id(name):
    with sqlite3.connect("speckweg.db") as connection:
        return connection.execute(
            "SELECT id FROM users WHERE name = ?", (name,)
        ).fetchall()


def get_users():
    with sqlite3.connect("speckweg.db") as connection:
        return connection.execute(
            "SELECT name FROM users"
        ).fetchall()


def get_history(user):
    with sqlite3.connect("speckweg.db") as connection:
        return connection.execute(
            "SELECT weight, date FROM weights WHERE user = ? ORDER BY date",
            (user,)
        ).fetchall()


def reset_db():
    connection = sqlite3.connect("speckweg.db")

    connection.execute("DROP TABLE IF EXISTS users")
    connection.execute("DROP TABLE IF EXISTS weights")

    connection.commit()
    connection.close()

    initialize()


def get_latest_weight(user):
    with sqlite3.connect("speckweg.db") as connection:
        return connection.execute(
            "SELECT weight FROM weights WHERE user = ? ORDER BY date DESC, id DESC LIMIT 1",
            (user,)
        ).fetchone()
