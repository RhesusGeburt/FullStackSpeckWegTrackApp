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
            height INTEGER,
            target_weight REAL
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

    # Prüfen, ob target_weight bereits existiert
    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]

    if "target_weight" not in columns:
        cursor.execute(
            "ALTER TABLE users ADD COLUMN target_weight REAL"
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
    connection = sqlite3.connect("speckweg.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name) VALUES (?)",
        (name,),
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


def delete_user(user_id):
    with sqlite3.connect("speckweg.db") as connection:
        connection.execute(
            "DELETE FROM weights WHERE user = ?",
            (user_id,)
        )

        connection.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )


def get_start_weight(user):
    with sqlite3.connect("speckweg.db") as connection:
        return connection.execute(
            """
            SELECT weight
            FROM weights
            WHERE user = ?
            ORDER BY date ASC, id ASC
            LIMIT 1
            """,
            (user,)
        ).fetchone()


def set_target_weight(user_id, weight):
    with sqlite3.connect("speckweg.db") as connection:
        connection.execute(
            "UPDATE users SET target_weight = ? WHERE id = ?",
            (weight, user_id)
        )


def get_target_weight(user_id):
    with sqlite3.connect("speckweg.db") as connection:
        return connection.execute(
            "SELECT target_weight FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()
