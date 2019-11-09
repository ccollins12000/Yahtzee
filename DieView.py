from tkinter import *
from tkinter import ttk as tk

class DieView:
    """
    This is a class to display a single die that can be selected

    Attributes:
        selected (bool): Whether or not the die is selected
        last_roll (int): The number diplayed on the die

    """
    def __init__(self, master, initial_roll=6):
        self._last_roll = initial_roll
        self._image = PhotoImage(file="Die" + str(self._last_roll) + "_selected.png")
        self._selected = IntVar(value=1)
        self.view = tk.Label(master, image=self._image)
        #self.view = tk.Checkbutton(master, image=self._image, variable=self._selected)
        self.view.bind("<Button-1>", self.toggle_selected)

    def set_image(self, value, selected):
        if selected == 1:
            self._image = PhotoImage(file="Die" + str(value) + "_selected.png")

        else:
            self._image = PhotoImage(file="Die" + str(value) + ".png")
        self.view.configure(image=self._image)

    def toggle_selected(self, event):
        if self._selected.get() == 1:
            self._selected.set(0)
        else:
            self._selected.set(1)
        self.set_image(self._last_roll, self._selected.get())


    @property
    def selected(self):
        """Get or set whether the die is selected. Toggles the checkbox control"""
        return self._selected.get()

    @selected.setter
    def selected(self, is_selected):
        self._selected.set(is_selected)
        self.set_image(self.last_roll, self._selected.get())

    @property
    def last_roll(self):
        """Get or set the number displayed on the die"""
        return self._last_roll

    @last_roll.setter
    def last_roll(self, value):
        if 1 <= value <= 6:
            self._last_roll = value
            self.set_image(self._last_roll, self._selected.get())
        else:
            raise Exception('Value of die view must be between 1 and 6')

