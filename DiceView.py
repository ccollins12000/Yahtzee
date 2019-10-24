from tkinter import *
from tkinter import ttk as tk

from tkinter import *
from tkinter import ttk as tk

yahtzee = Tk()
dice_board_gui = tk.Frame(yahtzee)
dice_board_gui.pack()
die_img = PhotoImage(file="Die6.png")
die_img = PhotoImage(file="Die5.png")
dice = {}


class DieView:
    def __init__(self, master, value):
        self.image = PhotoImage(file="Die6.png")
        self.view = tk.Checkbutton(master, image=self.image)

    def update_value(self, value):
        self.image = PhotoImage(file="Die" + str(value) + ".png")
        self.view.configure(image=self.image)


class DiceView:
    def __init__(self, master):
        self.dice = []
        for die_index in range(5):
            self.dice.append(DieView(master, 6))
            self.dice[die_index].view.pack()
        self.btn_roll = tk.Button(master, text="Roll Dice")
        self.btn_roll.pack()



diceview = DiceView(dice_board_gui)


yahtzee.mainloop()