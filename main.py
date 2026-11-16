import database as db
import datetime as date

db.initialize()
db.add_user("Jakob", 25, 182)
jakob = int(db.get_id("Jakob")[0][0])
db.add_weight(jakob, 79.2, date.datetime.now())

jakob_history = db.get_history(jakob)

print(jakob_history, type(jakob_history))
