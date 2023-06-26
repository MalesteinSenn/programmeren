import tkinter as tk
from tkinter import *
import turtle
from turtle import *

import random
from random import randrange

import opdracht6_AKAR

import eindopdrachtsenn





# Maak een nieuw window met een titel
window = Tk()
window.title("Menu SpaceCase")

# Begin Frame

frame_begin = tk.Frame(borderwidth=10)
welkom = tk.Label(frame_begin, text="Welkom bij onze menu!!")
welkom.pack()

welkom2 = tk.Label(frame_begin, text="In het menu kan je wissellen naar een andere functie!")
welkom2.pack()

frame_begin.pack()

#FRAME SENN

frame_Senn = Frame(borderwidth=10)
test = eindopdrachtsenn.tekenen(frame_Senn)
frame_Senn = test.returnFrame()






# FRAME VOOR THING 3 --------------------------------
frame_akkar = opdracht6_AKAR.Application(window)



# FRAME VOOR THING 4 --------------------------------


frame_thing_4 = tk.Frame(borderwidth=10)

frame_thing_4.columnconfigure(index=0, weight=1)
frame_thing_4.columnconfigure(index=1, weight=1)
frame_thing_4.columnconfigure(index=2, weight=1)

label_out = tk.Label(frame_thing_4, text="Dit is een getallen raden spel!", font=("Helvetica", 16))
label_out.pack(pady=20)

label = tk.Label(frame_thing_4, text="Voer een getal in tussen de 1 en 13", font=("Helvetica", 12))
label.pack()

entry = tk.Entry(master=frame_thing_4, width=10, font=("Helvetica", 12))
entry.pack(pady=10)

btn_submit = tk.Button(master=frame_thing_4, text="Start", font=("Helvetica", 12), bg="green", fg="white")
btn_submit.pack(pady=10)

btn_clear = tk.Button(master=frame_thing_4, text="Probeer opnieuw!", font=("Helvetica", 12), bg="red", fg="white", command=lambda: reset_game())
btn_clear.pack(pady=10)

te_raden_getal = randrange(1, 13)
pogingen = 0

# Label voor het aantal pogingen
label_pogingen = tk.Label(frame_thing_4, text="Aantal pogingen: {}".format(pogingen), font=("Helvetica", 12))
label_pogingen.pack()

# Label voor de geraden waarde
label_geraden = tk.Label(frame_thing_4, text="", font=("Helvetica", 12))
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



# Functies voor het menu
def show_thing_1():
     frame_Senn.pack_forget()
     frame_akkar.pack_forget()
     frame_thing_4.pack_forget()
     frame_thing_1.pack()
    

def show_frame_Senn():
    frame_Senn.pack()
    frame_thing_1.pack_forget()
    frame_akkar.pack_forget()
    frame_thing_4.pack_forget()

def show_frame_akkar():
    frame_akkar.pack()
    frame_thing_1.pack_forget()
    frame_Senn.pack_forget()
    frame_thing_4.pack_forget()

def show_thing_4():
    frame_thing_4.pack()
    frame_thing_1.pack_forget()
    frame_Senn.pack_forget()
    frame_akkar.pack_forget()

# Menu maken
menubar = Menu(window)
window.config(menu=menubar)

# Menu items maken
mainmenu = Menu(menubar)
mainmenu.add_command(label="Frame Jonno", command=show_thing_1)
mainmenu.add_command(label="Frame Senn", command=show_frame_Senn) 
mainmenu.add_command(label="Frame Akar", command=show_frame_akkar)
mainmenu.add_command(label="Frame Tomas", command=show_thing_4)         
mainmenu.add_separator()
mainmenu.add_command(label="Exit", command=window.quit)
# Menu toevoegen aan menubar
menubar.add_cascade(label="Tool", menu=mainmenu)





# FRAME VOOR THING 1 --------------------------------
frame_thing_1 = tk.Frame(borderwidth=10)
frame_thing_1.columnconfigure(index=0, weight=1)
frame_thing_1.columnconfigure(index=1, weight=1)


# Initialiseer de tkinter-toepassing

# Maak een label om het aantal ogen op de dobbelsteen weer te geven
label = tk.Label(frame_thing_1, font=("Helvetica", 72), text="")
label.pack()




# Functie voor het rollen van 1 dobbelsteen
def roll_1dice():
    roll_result = random.randint(1, 6) # Genereer een willekeurig getal tussen 1 en 6
    label.config(text=str(roll_result)) # Geef het resultaat weer op het label

# Maak een knop om de dobbelsteen te rollen
button = tk.Button(frame_thing_1, text="Gooi 1 dobbelsteen", command=roll_1dice)
button.pack()

# Functie voor het rollen van 2 dobbelstenen
def roll_2dice():
    roll_result = sum([random.randint(1, 6) for _ in range(2)]) # Gooi 2 dobbelstenen en tel de resultaten op
    label.config(text=str(roll_result)) # Geef het resultaat weer op het label

# Maak een knop om 2 dobbelstenen te rollen
button_2dice = tk.Button(frame_thing_1, text="Gooi 2 dobblesteen", command=roll_2dice)
button_2dice.pack()

# Functie voor het rollen van 3 dobbelstenen
def roll_3dice():
    roll_result = sum([random.randint(1, 6) for _ in range(3)]) # Gooi 3 dobbelstenen en tel de resultaten op
    label.config(text=str(roll_result)) # Geef het resultaat weer op het label

# Maak een knop om 3 dobbelstenen te rollen
button_3dice = tk.Button(frame_thing_1, text="Gooi 3 dobbelsteen", command=roll_3dice)
button_3dice.pack()

# Start de tkinter-toepassing
window.mainloop()



# MAIN --------------------------------
# Begin met frame 1
show_thing_1()
# Start the application
window.mainloop()