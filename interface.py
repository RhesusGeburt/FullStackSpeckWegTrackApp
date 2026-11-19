from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import database as db
from datetime import datetime
import main
import graph

main.start()

root = tk.Tk()
root.title("FullStackSpeckWegTrackApp 1.0.75")
root.geometry("1000x700")
root.minsize(700, 500)
root.state("zoomed")
root.configure(bg="#121417")

BG = "#1C2025"
CARD = "#252B32"
INPUT = "#191D22"
PRIMARY = "#3B82F6"
HOVER = "#60A5FA"
WHITE = "#F9FAFB"
LIGHT_TEXT = "#A1A1AA"

karte = tk.Frame(root, bg=CARD, padx=60, pady=45)
karte.place(relx=0.5, rely=0.5, anchor="center")


def gewicht_seite():

    for widget in karte.winfo_children():
        widget.destroy()

    titel = tk.Label(karte, text="Gewicht eintragen", font=(
        "Arial", 32, "bold"), fg=WHITE, bg=CARD)
    titel.pack(pady=(10, 15))

    untertitel = tk.Label(karte, text="Trage dein aktuelles Gewicht ein!", font=(
        "Arial", 13), fg="#aaaac0", bg=CARD)
    untertitel.pack(pady=(0, 30))

    gewicht_eingabe = tk.Entry(karte, font=("Arial", 16), bg=INPUT, fg=WHITE,
                               insertbackground=WHITE, relief="flat", width=25,
                               justify="center")
    gewicht_eingabe.pack(pady=15, ipady=12)

    einheit = tk.Label(karte, text="Gewicht in kg", font=(
        "Arial", 12), fg=LIGHT_TEXT, bg=CARD)
    einheit.pack()

    speichern = tk.Button(karte, text="Speichern", font=("Arial", 14, "bold"),
                          bg=LIGHT_TEXT, fg=WHITE, relief="flat", cursor="hand2",
                          padx=35, pady=12)
    speichern.pack(pady=20)

    zurueck = tk.Button(karte, text="Zurück", font=("Arial", 12), bg=CARD,
                        fg=LIGHT_TEXT, relief="flat", cursor="hand2",
                        command=startseite)
    zurueck.pack(pady=10)


def dashboard(username, user_id):

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#121820")

    sidebar = tk.Frame(root, bg="#1B2430", width=230)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    hauptbereich = tk.Frame(root, bg="#121820")
    hauptbereich.pack(side="left", fill="both", expand=True)

    titel = tk.Label(sidebar, text="SPECKWEG", font=(
        "Arial", 22, "bold"), fg=WHITE, bg="#1B2430")
    titel.pack(pady=40)

    dashboard_button = tk.Button(sidebar, text="Dashboard", font=(
        "Arial", 13), bg="#252F3B", fg=WHITE, relief="flat")
    dashboard_button.pack(fill="x", padx=15, pady=8)

    gewicht_button = tk.Button(sidebar, text="Gewicht", font=("Arial", 13),
                               bg="#1B2430", fg=WHITE, relief="flat",
                               command=lambda: gewicht_anzeigen(username, user_id))
    gewicht_button.pack(fill="x", padx=15, pady=8)

    historie_button = tk.Button(sidebar, text="Historie", font=(
        "Arial", 13), bg="#1B2430", fg=WHITE, relief="flat",
        command=lambda: historie_anzeigen(username, user_id))
    historie_button.pack(fill="x", padx=15, pady=8)

    profil_button = tk.Button(sidebar, text="Profil", font=(
        "Arial", 13), bg="#1B2430", fg=WHITE, relief="flat")
    profil_button.pack(fill="x", padx=15, pady=8)

    einstellungen_button = tk.Button(sidebar, text="Einstellungen", font=(
        "Arial", 13), bg="#1B2430", fg=WHITE, relief="flat")
    einstellungen_button.pack(fill="x", padx=15, pady=8)

    ueberschrift = tk.Label(hauptbereich, text="Dashboard", font=(
        "Arial", 30, "bold"), fg=WHITE, bg="#121820")
    ueberschrift.pack(anchor="w", padx=50, pady=40)

    begrüssung = tk.Label(hauptbereich, text=f"Willkommen zurück, {username}!", font=(
        "Arial", 16, "bold"), fg="#94A3B8", bg="#121820")
    begrüssung.pack(anchor="ne", padx=50, pady=10)

    untertitel = tk.Label(hauptbereich, text="Willkommen bei Speckweg!", font=(
        "Arial", 14), fg="#94A3B8", bg="#121820")
    untertitel.pack(anchor="w", padx=50)

    kartenbereich = tk.Frame(hauptbereich, bg="#121820")
    kartenbereich.pack(anchor="nw", padx=50, pady=30)

    karte = tk.Frame(kartenbereich, bg="#252F3B", padx=30, pady=25,
                     width=450, height=180, highlightbackground="#3B82F6",
                     highlightthickness=1)
    karte.pack(side="left", padx=(0, 20))
    karte.pack_propagate(False)

    gewicht_titel = tk.Label(karte, text="Aktuelles Gewicht", font=(
        "Arial", 13), fg="#94A3B8", bg="#252F3B")
    gewicht_titel.pack(anchor="w")

    letztes_gewicht = db.get_latest_weight(user_id)

    if letztes_gewicht:
        gewicht_text = f"{letztes_gewicht[0]} kg"
    else:
        gewicht_text = "Noch kein Gewicht eingetragen"

    gewicht_wert = tk.Label(karte, text=gewicht_text, font=(
        "Arial", 20, "bold"), fg=WHITE, bg="#252F3B")
    gewicht_wert.pack(anchor="w", pady=(10, 0))

    karte2 = tk.Frame(kartenbereich, bg="#252F3B", padx=30, pady=25, width=450,
                      height=180, highlightbackground="#3B82F6", highlightthickness=1)
    karte2.pack(side="left")
    karte2.pack_propagate(False)

    fortschritt_titel = tk.Label(karte2, text="Dein Fortschritt", font=(
        "Arial", 13), fg="#94A3B8", bg="#252F3B")
    fortschritt_titel.pack(anchor="w")

    fortschritt_wert = tk.Label(karte2, text="Noch keine Daten vorhanden", font=(
        "Arial", 16, "bold"), fg=WHITE, bg="#252F3B")
    fortschritt_wert.pack(anchor="w", pady=(10, 0))

    karte2 = tk.Frame(kartenbereich, bg="#252F3B", padx=30, pady=25, width=450,
                      height=180, highlightbackground="#3B82F6",
                      highlightthickness=1)
    karte2.pack(side="left")
    karte2.pack_propagate(False)
    fortschritt_titel = tk.Label(karte2, text="Dein Fortschritt", font=(
        "Arial", 13), fg="#94A3B8", bg="#252F3B")
    fortschritt_titel.pack(anchor="w")

    fortschritt_wert = tk.Label(karte2, text="Noch keine Daten vorhanden", font=(
        "Arial", 16, "bold"), fg=WHITE, bg="#252F3B")
    fortschritt_wert.pack(anchor="w", pady=(10, 0))


def gewicht_anzeigen(username, user_id):

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#121820")

    hauptbereich = tk.Frame(root, bg="#121820")
    hauptbereich.pack(fill="both", expand=True)

    zurueck_button = tk.Button(hauptbereich, text="← Zurück zum Dashboard",
                               font=("Arial", 12), bg="#1B2430", fg=WHITE,
                               activebackground="#252F3B", relief="flat",
                               cursor="hand2", padx=20, pady=10,
                               command=lambda: dashboard(username, user_id))
    zurueck_button.pack(anchor="w", padx=50, pady=(20, 0))

    titel = tk.Label(hauptbereich, text="Gewicht eintragen",
                     font=("Arial", 30, "bold"), fg=WHITE, bg="#121820")
    titel.pack(anchor="w", padx=50, pady=(50, 10))

    untertitel = tk.Label(hauptbereich, text="Trage dein aktuelles Gewicht ein!", font=(
        "Arial", 14), fg="#94A3B8", bg="#121820")
    untertitel.pack(anchor="w", padx=50, pady=(0, 30))

    eingabekarte = tk.Frame(hauptbereich, bg="#252F3B",
                            padx=40, pady=35, width=450, height=300)
    eingabekarte.pack(anchor="nw", padx=50, pady=20)
    eingabekarte.pack_propagate(False)

    gewicht_titel = tk.Label(eingabekarte, text="Dein Gewicht", font=(
        "Arial", 15, "bold"), fg=WHITE, bg="#252F3B")
    gewicht_titel.pack(anchor="w", pady=(0, 15))

    gewicht_eingabe = tk.Entry(eingabekarte, font=("Arial", 18), bg="#18212B",
                               fg=WHITE, insertbackground=WHITE, relief="flat",
                               width=20, justify="center")
    gewicht_eingabe.pack(pady=10, ipady=10)

    einheit = tk.Label(eingabekarte, text="Angabe in Kilogramm (kg)", font=(
        "Arial", 11), fg="#94A3B8", bg="#252F3B")
    einheit.pack()

    ausgabe = tk.Label(eingabekarte, text="", font=(
        "Arial", 11), fg="#4ADE80", bg="#252F3B")
    ausgabe.pack(pady=5)

    def speichern():

        try:
            gewicht = float(gewicht_eingabe.get().replace(",", "."))

            if gewicht <= 0:
                ausgabe.config(
                    text="Bitte gib ein gültiges Gewicht ein!", fg="#ff6b81")
                return

            db.add_weight(user_id, gewicht, datetime.now())

            ausgabe.config(
                text="Gewicht erfolgreich gespeichert!", fg="#4ADE80")
            gewicht_eingabe.delete(0, tk.END)

        except ValueError:
            ausgabe.config(
                text="Bitte gib eine gültige Zahl ein!", fg="#ff6b81")

    speichern_button = tk.Button(eingabekarte, text="Gewicht speichern",
                                 font=("Arial", 14, "bold"), bg=PRIMARY,
                                 fg=WHITE, activebackground=HOVER, relief="flat",
                                 cursor="hand2", padx=25, pady=12, command=speichern)
    speichern_button.pack(pady=10)


def historie_anzeigen(username, user_id):

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#121820")

    fig1 = graph.make_graph(user_id)

    hauptbereich = tk.Frame(root, bg="#121820")
    hauptbereich.pack(fill="both", expand=True)

    zurueck_button = tk.Button(hauptbereich, text="← Zurück zum Dashboard",
                               font=("Arial", 12), bg="#1B2430", fg=WHITE,
                               activebackground="#252F3B", relief="flat",
                               cursor="hand2", padx=20, pady=10,
                               command=lambda: dashboard(username, user_id))
    zurueck_button.pack(anchor="w", padx=50, pady=(20, 0))

    titel = tk.Label(hauptbereich, text="Dein Fortschritt",
                     font=("Arial", 30, "bold"), fg=WHITE, bg="#121820")
    titel.pack(anchor="w", padx=50, pady=(50, 10))

    fig1.set_size_inches(12, 7)

    canvas = FigureCanvasTkAgg(fig1, master=hauptbereich)
    canvas.draw()

    canvas.get_tk_widget().pack(
        anchor="nw",
        padx=50,
        pady=20,
        fill="both",
        expand=True
    )


def startseite():

    for widget in karte.winfo_children():
        widget.destroy()

    titel = tk.Label(karte, text="Willkommen!", font=(
        "Arial", 32, "bold"), fg=WHITE, bg=CARD)
    titel.pack(pady=(10, 15))

    untertitel = tk.Label(karte, text="Schön, dass du da bist!", font=(
        "Arial", 13), fg="#aaaac0", bg=CARD)
    untertitel.pack(pady=(0, 30))

    eingabe = tk.Entry(karte, font=("Arial", 16), bg=INPUT, fg=WHITE,
                       insertbackground=WHITE, relief="flat", width=25, justify="center")
    eingabe.pack(pady=15, ipady=12)

    ausgabe = tk.Label(karte, text="", font=(
        "Arial", 20, "bold"), fg=LIGHT_TEXT, bg=CARD)
    ausgabe.pack(pady=20)

    def ask_username():

        username = eingabe.get().strip()

        if len(username) < 3:
            ausgabe.config(
                text="Username muss mindestens 3 Zeichen haben!", fg="#ff6b81")
            return

        elif len(username) > 30:
            ausgabe.config(
                text="Username darf maximal 30 Zeichen haben!", fg="#ff6b81")
            return

        user_id = db.get_id(username)

        if user_id:
            ausgabe.config(
                text=f"Willkommen zurück, {username}!", fg=LIGHT_TEXT)

        else:
            db.add_user(username)
            ausgabe.config(
                text=f"Neuer Benutzer {username} wurde erstellt!", fg=LIGHT_TEXT)

        user_id = db.get_id(username)[0][0]
        dashboard(username, user_id)

    button = tk.Button(karte, text="Bestätigen", command=ask_username,
                       font=("Arial", 14, "bold"), bg=LIGHT_TEXT,
                       fg=WHITE, activebackground=HOVER, activeforeground=WHITE,
                       relief="flat", cursor="hand2", padx=35, pady=12)
    button.pack(pady=20)

    def hover_on(event):
        button.config(bg=HOVER)

    def hover_off(event):
        button.config(bg=LIGHT_TEXT)

    button.bind("<Enter>", hover_on)
    button.bind("<Leave>", hover_off)

    root.bind("<Return>", lambda event: ask_username())

    eingabe.focus_set()


startseite()

root.mainloop()
