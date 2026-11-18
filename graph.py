import matplotlib.dates as mdates
import matplotlib.ticker
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,                                               NavigationToolbar2Tk)
import database as db
from datetime import datetime

def make_graph(userID):
    history = db.get_history(userID)
    fig = Figure(figsize=(5, 5), dpi=100)

    if len(history) < 2:
        fig.text(
            0.5, 0.5,
            "Not enough data has been collected.",
            ha="center",
            va="center",
            fontsize=12
        )
        return fig

    weights, dates = zip(*history)

    dates = [datetime.fromisoformat(date) for date in dates]

    plot1 = fig.add_subplot()

    locator = mdates.AutoDateLocator(maxticks=5)
    formatter = mdates.DateFormatter("%d.%m.%y")
    fig.autofmt_xdate(rotation=45)

    plot1.xaxis.set_major_locator(locator)
    plot1.xaxis.set_major_formatter(formatter)

    plot1.set_ylabel("Weight in kg")
    plot1.set_xlabel("Time")

    plot1.plot(dates, weights)

    return fig
