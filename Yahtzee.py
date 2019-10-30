from tkinter import *
from tkinter import ttk as tk
import YahtzeeViews
import YahtzeeModel


def empty_function():
    pass


class Yahtzee():
    def __init__(self, tk_master):
        self._view = YahtzeeViews.YahtzeeView(tk_master, self.roll_dice ,empty_function ,empty_function)
        self._model = YahtzeeModel.YahtzeeModel()
        self.roll_dice()

    def update_dice_select(self):
        for die_index in range(5):
            if self._view.die_selected(die_index) == 1:
                view_selected = True
            else:
                view_selected = False
            self._model.toggle_die_for_roll(die_index, view_selected)

    def roll_dice(self):
        self.update_dice_select()
        dice_values = self._model.roll_dice()
        for die_index, die_value in enumerate(dice_values):
            self._view.update_die(die_index, die_value)


yahtzee_tk = Tk()
y = Yahtzee(yahtzee_tk)
yahtzee_tk.mainloop()
