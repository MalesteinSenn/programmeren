import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
     

    def create_widgets(self):
        self.label = tk.Label(self, text="Raad de naam van een vrucht. (Je hebt maximaal 5 pogingen!)")
        self.label.pack()
        self.entry = tk.Entry(self, width=5)
        self.entry.pack()

        self.raden_button = tk.Button(self, text="Raden", command=self.woordRaden)
        self.raden_button.pack(side="bottom")

        self.quit_button = tk.Button(self, text="Afsluiten", command=self.master.quit)
        self.quit_button.pack(side="bottom")

        self.antwoord_label = tk.Label(self, text="")
        self.antwoord_label.pack()

        self.pogingen_label = tk.Label(self, text="Pogingen: 5")
        self.pogingen_label.pack()

    def woordRaden(self):
        geradenWoord = self.entry.get()
        if geradenWoord in self.woorden and geradenWoord not in self.geraden_woorden:
            self.punten += 1
            self.antwoord_label.configure(text="GOED")
            self.geraden_woorden.append(geradenWoord)

        elif geradenWoord in self.geraden_woorden:
            self.antwoord_label.configure(text="Dit woord is al geraden")

        else:
            self.antwoord_label.configure(text="FOUT")
        self.pogingen -= 1

        self.pogingen_label.configure(text="Pogingen: " + str(self.pogingen))

        if self.punten == 5:
            self.antwoord_label.configure(text="Je hebt het maximale aantal punten bereikt.")
            self.raden_button["state"] = "disabled"
            return

        if self.pogingen == 0:
            self.antwoord_label.configure(text="Je hebt " + str(self.punten) + " punten gehaald. Maximum aantal gokken bereikt.")
            self.raden_button["state"] = "disabled"
            return

    woorden = ["appel", "peer", "aardbei", "watermeloen", "banaan"]
    punten = 0
    pogingen = 5
    geraden_woorden = []

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
