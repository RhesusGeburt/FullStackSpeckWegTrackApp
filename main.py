import database as db


def start():
    db.initialize()

    print("Benutzer:")
    print(db.get_users())

    print("Benutzer-ID von Jakob:")
    print(db.get_id("Jakob"))
