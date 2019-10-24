from tkinter import *
from tkinter import ttk as tk

from tkinter import *
from tkinter import ttk as tk

yahtzee = Tk()
dice_board_gui = tk.Frame(yahtzee)
dice_board_gui.pack()
die_img = PhotoImage(file="Die.png")
dice = {}


class DieView:
    def __init__(self, master, value):
        self.image = PhotoImage(file="Die.png")
        self.view = tk.Checkbutton(master, image=die_img)


class DiceView:
    def __init__(self, master):
        for i in range(5):
            die = DieView(master, 6)
            die.view.pack()
        self.btn_roll = tk.Button(master, text="Roll Dice")
        self.btn_roll.pack()

diceview = DiceView(dice_board_gui)

yahtzee.mainloop()