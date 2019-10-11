from tkinter import *
from tkinter import ttk as tk

from tkinter import *
from tkinter import ttk as tk

yahtzee = Tk()
dice_board_gui = tk.Frame(yahtzee)
dice_board_gui.pack()
die_img = PhotoImage(file="Die.png")
dice = {}

for die_index in range(1,6):
    selected = IntVar()
    dice[("die" + str(die_index))] = [selected, tk.Checkbutton(image=die_img)]

for die in dice:
    dice[die][1].pack()
    dice[die][0].set(0)

btn_roll = tk.Button(text="Roll Dice")
btn_roll.pack()
yahtzee.mainloop()