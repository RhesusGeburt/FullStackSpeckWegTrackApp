import graph
import database as db
import datetime
import tkinter as tk
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# db.add_user("GraphTest", "Admin")
id = db.get_id("GraphTest")[0][0]
for i in range(30, 60):
    time = datetime.datetime.now() + datetime.timedelta(days=i)
    # db.add_weight(id, random.randint(70, 90), time)

graph = graph.make_graph(id)

root = tk.Tk()
canvas = FigureCanvasTkAgg(graph, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

root.mainloop()
