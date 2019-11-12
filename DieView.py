"""This is a module contains all the code for displaying a die object

"""

from tkinter import *
from tkinter import ttk as tk

class DieView:
    """
    This is a class to display a single die that can be selected

    Attributes:
        view (obj:): The Tkinter label object containing the die image
    """
    def __init__(self, master, initial_roll=6):
        """
        The constructor for a die object

        Args:
            master (obj): The Tkinter master object the die will be displayed in
            initial_roll (int:) The initial display for the die object.  Default of 6

        Raises:
            Exception: If the value is not between 1 and 6, an error is raised.  This isn't some fancy D&D game, it's just a boring old Yahtzee game!
        """
        self._last_roll = initial_roll
        self._image = PhotoImage(file="Die" + str(self._last_roll) + "_selected.png")
        self._selected = IntVar(value=1)
        self.view = tk.Label(master, image=self._image)
        self.view.bind("<Button-1>", self.toggle_selected)

    def set_image(self, value, selected):
        """Helper function for changing the die roll value to display

        Note:
            Use toggle selected and last roll to update the die.  This is just a helper function for within the class

        Args:
            value (int): The value to display on the die
            selected (bool): Whether or not the die shows as selected
        """
        if selected == 1:
            self._image = PhotoImage(file="Die" + str(value) + "_selected.png")

        else:
            self._image = PhotoImage(file="Die" + str(value) + ".png")
        self.view.configure(image=self._image)

    def toggle_selected(self, event):
        """Helper function for changing whether the die shows as selected or not

        Note:
            Don't utilize this function.  It is what is bound to the image clicked event

        Args:
            event (obj): A Tkinter event triggering unselecting or selecting the die.
        """
        if self._selected.get() == 1:
            self._selected.set(0)
        else:
            self._selected.set(1)
        self.set_image(self._last_roll, self._selected.get())


    @property
    def selected(self):
        """bool: Get or set whether the die is selected."""
        return self._selected.get()

    @selected.setter
    def selected(self, is_selected):
        self._selected.set(is_selected)
        self.set_image(self.last_roll, self._selected.get())

    @property
    def last_roll(self):
        """int: Get or set the number displayed on the die"""
        return self._last_roll

    @last_roll.setter
    def last_roll(self, value):
        if 1 <= value <= 6:
            self._last_roll = value
            self.set_image(self._last_roll, self._selected.get())
        else:
            raise Exception('Value of die view must be between 1 and 6')

