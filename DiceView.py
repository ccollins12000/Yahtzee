from tkinter import *
from tkinter import ttk as tk
import Die
from tkinter import *
from tkinter import ttk as tk


class DieView:
    def __init__(self, master, value=None):
        if value is None:
            value = 6
        self.image = PhotoImage(file="Die" + str(value) + ".png")
        self.selected = IntVar()
        self.view = tk.Checkbutton(master, image=self.image, variable=self.selected)

    def update_value(self, value):
        self.image = PhotoImage(file="Die" + str(value) + ".png")
        self.view.configure(image=self.image)


class DiceView:
    def __init__(self, master, number_of_dice, initial_rolls, roll_fun):
        self.dice = []
        self._can_roll = True
        self._rolls_remaining = initial_rolls
        for die_index in range(number_of_dice):
            self.dice.append(DieView(master))
            self.dice[-1].view.pack()
        self._rollsRemainingTxt = StringVar()
        self._rollsRemainingTxt.set('Rolls Remaining: ' + str(initial_rolls))
        self._txt_rolls_remaining = tk.Label(master, textvariable=self._rollsRemainingTxt)
        self._txt_rolls_remaining.pack()
        self.btn_roll = tk.Button(master, text="Roll Dice", command=roll_fun)
        self.btn_roll.pack()

    @property
    def rolls_remaining(self):
        return self._rolls_remaining

    @rolls_remaining.setter
    def rolls_remaining(self, value):
        self._rolls_remaining = value
        self._rollsRemainingTxt.set('Rolls Remaining: ' + str(self._rolls_remaining))

    @property
    def can_roll(self):
        return self._can_roll

    @can_roll.setter
    def can_roll(self, enabled):
        self._can_roll = enabled
        if enabled:
            self.btn_roll.config(state=NORMAL)
        else:
            self.btn_roll.config(state=DISABLED)
