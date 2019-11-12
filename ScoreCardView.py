

from tkinter import *
from tkinter import ttk as tk

score_box_view_types = {'Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a Kind', '4 of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance'}


class ScoreBoxView:
    """
    This is a class for an individual score box on a Yahtzee score sheet

    Attributes:
        name (str): The name of the score box
    """

    def __init__(self, master, name, can_assign: bool, assignment_var: StringVar):
        """
        The constructor for ScoreBoxView

        Notes:
            The score box label and points box must manaully be grid into the master score card object to display

        Args:
            points_view (:obj:): The Tkinter entry object containing the points
            selector (:obj:): The label object containing the picture/text for the scorebox
        """
        self._name = name
        self._enabled = False
        self._can_assign = can_assign
        self.points_view = tk.Entry(master, width=3, state='disabled')
        self._assignment_var = assignment_var
        self._image = PhotoImage(file="Score_Box_Images/" + name + ".png")
        self.selector = tk.Label(master, image=self._image, borderwidth=3, relief=RAISED, background = 'BLACK')
        self.selector.bind("<Button-1>", self.select)

    def select(self, event):
        """Helper function for when the image gets clicked. Sets the selected box for the score card when the box is clicked.

        Note:
            Do not utilize this method outside of the class.  The score box image has this function bound via the tkinter button1 event.

        Args:
            event: tkinter event. When the scorebox image is clicked
        """
        self._assignment_var.set(self._name)

    def set_image(self, selected):
        """Helper function for when the image gets clicked.  Sets the image to show whether the box is selected or not.

        Note:
            Do not utilize this method outside of the class

        Args:
            selected: Whether or not the box is selected
        """
        if selected and self._can_assign and self.enabled:
            self.selector.configure(background='RED', relief=SUNKEN)
        else:
            self.selector.configure(background='BLACK', relief=RAISED)

    @property
    def assignable(self):
        """bool: Get whether or not points can be assigned by the player to the box"""
        return self._can_assign

    @property
    def points(self):
        """int: Get or set the points displayed in the score box"""
        return self.points_view.get()

    @points.setter
    def points(self, value):
        self.points_view.configure(state=NORMAL)
        self.points_view.delete(0, END)
        self.points_view.insert(0, value)
        self.points_view.configure(state=DISABLED)

    @property
    def enabled(self):
        """bool: Enabled or disable the score box from being able to be selected for assigning a dice roll"""
        return self._enabled

    @enabled.setter
    def enabled(self, enable):
        self._enabled = enable

    @property
    def name(self):
        """str: Get the name of the score box"""
        return self._name


class ScoreCardView:
    """
    This is a class for an the UI of a Yahtzee score sheet

    Attributes:
        selection (str): The name of the score box that is selected
    """
    def __init__(self, master):
        """
        The constructor for ScoreCardView

        Parameters:
            master (tk object): The tk master object to place the score card UI into
        """

        # dictionary of instructions for creating each score box
        box_setup_instructions = {
            'Aces': {'Can Assign': True, 'Section': 'Upper'},
            'Twos': {'Can Assign': True, 'Section': 'Upper'},
            'Threes': {'Can Assign': True, 'Section': 'Upper'},
            'Fours': {'Can Assign': True, 'Section': 'Upper'},
            'Fives': {'Can Assign': True, 'Section': 'Upper'},
            'Sixes': {'Can Assign': True, 'Section': 'Upper'},
            'Bonus': {'Can Assign': False, 'Section': 'Upper'},
            'Upper Total': {'Can Assign': False, 'Section': 'Upper'},
            '3 of a Kind': {'Can Assign': True, 'Section': 'Lower'},
            '4 of a Kind': {'Can Assign': True, 'Section': 'Lower'},
            'Full House': {'Can Assign': True, 'Section': 'Lower'},
            'Small Straight': {'Can Assign': True, 'Section': 'Lower'},
            'Large Straight': {'Can Assign': True, 'Section': 'Lower'},
            'Yahtzee': {'Can Assign': True, 'Section': 'Lower'},
            'Chance': {'Can Assign': True, 'Section': 'Lower'},
            'Lower Total': {'Can Assign': False, 'Section': 'Lower'},
            'Grand Total': {'Can Assign': False, 'Section': 'Lower'}
        }

        # Setup the main frame and variables
        self.mainFrame = tk.Frame(master)
        self.mainFrame.pack()
        self._assign_selection = StringVar()

        # create each score box
        self._score_boxes = {}
        for box_setup in box_setup_instructions:
            assignable = box_setup_instructions[box_setup]['Can Assign']
            self._score_boxes[box_setup] = ScoreBoxView(self.mainFrame, box_setup, assignable, self._assign_selection)

        # pack each score box into the frame
        rw = 0
        for scoreBox in self._score_boxes:
            self._score_boxes[scoreBox].points_view.grid(row=rw, column=1, sticky=NSEW)
            self._score_boxes[scoreBox].selector.grid(row=rw, column=0, sticky=NSEW)
            rw += 1

        # setup when the variable containing the scorebox selection is changed update the photos to reflect which box is selected
        self._assign_selection.trace('w', self.check_selection)

    def check_selection(self, *args):
        for box in self._score_boxes:
            if self.selection == box:
                self._score_boxes[box].set_image(True)
            else:
                self._score_boxes[box].set_image(False)

    @property
    def selection(self):
        """str: Get or set the selected score box on the score card.  Pass an empty string to deselect all boxes."""
        return self._assign_selection.get()

    @selection.setter
    def selection(self, box_name):
        self._assign_selection.set(box_name)

    def assign_points(self, box_name, points):
        """
        Update the number of points displayed in a score box on the score card UI

        Args:
            box_name (str): The name of the box to update the points in
            points (bool): the number of points to place in the score box UI
        """
        self._score_boxes[box_name].points = points

    def box_enabled(self, box_name, enabled):
        """
        Update whether or not a score box on the score card UI can be selected

        Args:
            box_name (str): The name of the box to disable/enable
            enabled (bool): Whether or not the box can be selected
        """
        self._score_boxes[box_name].enabled = enabled
