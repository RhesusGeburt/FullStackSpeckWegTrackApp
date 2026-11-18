import database as db
import math
import random
from datetime import datetime, timedelta


def start():
    db.initialize()

    # start = datetime.now() - timedelta(days=365)
    # for i in range (1, 360):
    #    weight = 90 + 5 * math.sin(i/30) + 2 *random.random() - i/36
    #    time = start + timedelta(days=i)
    #    db.add_weight(1, weight, time)
