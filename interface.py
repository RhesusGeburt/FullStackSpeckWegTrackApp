
import tkinter as tk
import database as db


root = tk.Tk()
root.title("Startseite")
root.geometry("1000x700")
root.minsize(700, 500)
root.state("zoomed")
root.configure(bg="#1e1e32")

BG = "#3f3f73"
CARD = "#2E2EF4"
INPUT = "#2c2c40"
PURPLE = "#7349dc"
HOVER = "#a78bfa"
WHITE = "#ffffff"
LIGHT_PURPLE = "#c0aef4"

karte = tk.Frame(root, bg=CARD, padx=60, pady=45
                 )

karte.place(relx=0.5, rely=0.5, anchor="center"
            )

titel = tk.Label(karte, text="Willkommen!", font=("Arial", 32, "bold"), fg=WHITE, bg=CARD
                 )

titel.pack(pady=(10, 15))

untertitel = tk.Label(karte, text="Schön, dass du da bist!",
                      font=("Arial", 13), fg="#aaaac0", bg=CARD)

untertitel.pack(pady=(0, 30))

eingabe = tk.Entry(karte, font=("Arial", 16), bg=INPUT, fg=WHITE,
                   insertbackground=WHITE, relief="flat", width=25, justify="center")

eingabe.pack(pady=15, ipady=12)


def ask_username():

    username = eingabe.get().strip()

    if len(username) < 3:

        ausgabe.config(
            text="Username muss mindestens 3 Zeichen haben!",
            fg="#ff6b81"
        )

    elif len(username) > 30:

        ausgabe.config(
            text="Username darf maximal 30 Zeichen haben!",
            fg="#ff6b81"
        )

    elif username:

        ausgabe.config(
            text=f"Hallo {username}!",
            fg=LIGHT_PURPLE
        )

        eingabe.delete(0, tk.END)

    else:

        ausgabe.config(
            text="Bitte Username eingeben!",
            fg="#ff6b81"
        )


button = tk.Button(karte, text="Bestätigen", command=ask_username,
                   font=("Arial", 14, "bold"), bg=PURPLE, fg=WHITE,
                   activebackground=HOVER,  activeforeground=WHITE, relief="flat",
                   cursor="hand2", padx=35, pady=12)

button.pack(pady=20)


def hover_on(event):
    button.config(bg=HOVER)


def hover_off(event):
    button.config(bg=PURPLE)


button.bind("<Enter>", hover_on)
button.bind("<Leave>", hover_off)

ausgabe = tk.Label(
    karte, text="", font=("Arial", 20, "bold"), fg=LIGHT_PURPLE, bg=CARD
)

ausgabe.pack(pady=20)

root.bind("<Return>", lambda event: ask_username())

eingabe.focus_set()

root.mainloop()
