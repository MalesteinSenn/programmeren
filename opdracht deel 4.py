import tkinter as tk
from random import randrange


window = tk.Tk()
window.title("Welkom bij ontspanningstool")


label_out = tk.Label(window, text="Dit is een getallen raden spel!", font=("Helvetica", 16))
label_out.pack(pady=20)

label = tk.Label(window, text="Voer een getal in tussen de 1 en 13", font=("Helvetica", 12))
label.pack()

entry = tk.Entry(master=window, width=10, font=("Helvetica", 12))
entry.pack(pady=10)

btn_submit = tk.Button(master=window, text="Start", font=("Helvetica", 12), bg="green", fg="white")
btn_submit.pack(pady=10)

btn_clear = tk.Button(master=window, text="Probeer opnieuw!", font=("Helvetica", 12), bg="red", fg="white", command=lambda: reset_game())
btn_clear.pack(pady=10)

te_raden_getal = randrange(1, 13)
pogingen = 0

# Label voor het aantal pogingen
label_pogingen = tk.Label(window, text="Aantal pogingen: {}".format(pogingen), font=("Helvetica", 12))
label_pogingen.pack()

# Label voor de geraden waarde
label_geraden = tk.Label(window, text="", font=("Helvetica", 12))
label_geraden.pack()

def handle_submit(event):
    global pogingen
    pogingen += 1
    ingevoerd_getal = int(entry.get())
    if ingevoerd_getal > te_raden_getal:
        label_geraden.config(text="Je hebt te hoog geraden", fg="red")
    elif ingevoerd_getal < te_raden_getal:
        label_geraden.config(text="Je hebt te laag geraden", fg="red")
    else:
        label_geraden.config(text="Je hebt het getal geraden, felicidades! Game is gestopt :)", fg="blue")
        btn_submit.config(state="disabled")
        return
    if pogingen >= 7:
        label_geraden.config(text="Jij hebt een maximale pogingen bereikt", fg="red")
        btn_submit.config(state="disabled")
        return
    # Update het label met het aantal pogingen
    label_pogingen.config(text="Aantal pogingen: {}".format(pogingen))
    label_geraden.config(text="Probeer het opnieuw! (poging {} van {})".format(pogingen, 7), fg="red")
    
def reset_game():
    global te_raden_getal, pogingen
    te_raden_getal = randrange(1, 13)
    pogingen = 0
    entry.delete(0, tk.END)
    label_pogingen.config(text="Aantal pogingen: {}".format(pogingen))
    label_geraden.config(text="")
    btn_submit.config(state="normal")

btn_submit.bind("<Button-1>", handle_submit)

window.configure(bg="white")  # achtergrondkleur van het venster
window.mainloop()

