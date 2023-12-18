import tkinter as tk
from tkinter import Label, Button
from random import randint

class DiceSimulator:
    def __init__(self, master):
        self.master = master

        # Etykieta do wyświetlania wyniku
        self.result_label = Label(master, text="", font=("Helvetica", 24))
        self.result_label.pack(pady = 30) # Padding górny wyniku

        # Przycisk do rzutu kostką
        self.roll_button = Button(master, text="Rzuć Kostką", command=self.roll_dice, padx=10, pady=10)
        self.roll_button.pack(side=tk.BOTTOM, pady=20) # Padding pod przyciskiem

    def roll_dice(self): # Losowanie wyniku
        result = randint(1, 6)
        self.result_label.config(text=str(result))

if __name__ == "__main__":
    root = tk.Tk()
    # Ustawienie minimalnego rozmiaru okna
    root.minsize(150, 200)
    app = DiceSimulator(root)
    root.mainloop()
