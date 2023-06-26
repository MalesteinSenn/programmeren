import random
import tkinter as tk

# Initialiseer de tkinter-toepassing
root = tk.Tk()
root.geometry("300x200")
root.title("Dobbellen")

# Maak een label om het aantal ogen op de dobbelsteen weer te geven
label = tk.Label(root, font=("Helvetica", 72), text="")
label.pack()


# Functie voor het rollen van 1 dobbelsteen
def roll_1dice():
    roll_result = random.randint(1, 6) # Genereer een willekeurig getal tussen 1 en 6
    label.config(text=str(roll_result)) # Geef het resultaat weer op het label

# Maak een knop om de dobbelsteen te rollen
button = tk.Button(root, text="Gooi 1 dobbelsteen", command=roll_1dice)
button.pack()

# Functie voor het rollen van 2 dobbelstenen
def roll_2dice():
    roll_result = sum([random.randint(1, 6) for _ in range(2)]) # Gooi 2 dobbelstenen en tel de resultaten op
    label.config(text=str(roll_result)) # Geef het resultaat weer op het label

# Maak een knop om 2 dobbelstenen te rollen
button_2dice = tk.Button(root, text="Gooi 2 dobblesteen", command=roll_2dice)
button_2dice.pack()

# Functie voor het rollen van 3 dobbelstenen
def roll_3dice():
    roll_result = sum([random.randint(1, 6) for _ in range(3)]) # Gooi 3 dobbelstenen en tel de resultaten op
    label.config(text=str(roll_result)) # Geef het resultaat weer op het label

# Maak een knop om 3 dobbelstenen te rollen
button_3dice = tk.Button(root, text="Gooi 3 dobbelsteen", command=roll_3dice)
button_3dice.pack()

# Start de tkinter-toepassing
root.mainloop()

