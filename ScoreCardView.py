

from tkinter import *
from tkinter import ttk as tk

score_box_view_types = {'Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a Kind', '4 of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance'}


class ScoreBoxView:
    """
    This is a class for an individual score box on a Yahtzee score sheet

    Attributes:
        name (str): The name of the score box
        frame (tk.frame): The tk frame object containing the score box UI elements
        points (int): The number of points in the scorebox
        enabled (bool): Whether or not the score box can be selected
    """

    def __init__(self, master, name, can_assign: bool, assignment_var: StringVar):
        """
        The constructor for ScoreBoxView

        Parameters:
            master (tk object): The tk master object to place the score box UI into
            name (str): The name of the score box, also displays as a text label next to the box on the UI. Should be one of the following values:
            'Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a Kind', '4 of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance'
            can_assign (bool): Whether a dice roll can be assigned to the score box (For Example: the grand total score box should have False passed here)
            assignment_var (tk StringVar): The variable where the selected score box will be stored. Passed from the larger score card view object.
        """
        self._name = name
        self._image = PhotoImage(file="Score_Box_Images/" + name + ".png")

        self.points_view = tk.Entry(master, width=3, state='disabled')
        # if can_assign:
        #     self.selector = tk.Radiobutton(master, variable=assignment_var, text=name, width=11, value=name)
        # else:
        #     self.selector = tk.Label(master, text=name, width=13)
        self.selector = tk.Label(master, image=self._image)
    @property
    def points(self):
        """Get or set the points displayed in the score box"""
        return self.points_view.get()

    @points.setter
    def points(self, value):
        self.points_view.configure(state=NORMAL)
        self.points_view.delete(0, END)
        self.points_view.insert(0, value)
        self.points_view.configure(state=DISABLED)

    @property
    def enabled(self):
        """Enabled or disable the score box from being able to be selected for assigning a dice roll"""
        return self.selector.state()

    @enabled.setter
    def enabled(self, enable):
        if enable:
            self.selector.configure(state=NORMAL)
        else:
            self.selector.configure(state=DISABLED)

    @property
    def name(self):
        """Get the name of the score box"""
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
        rw = 0

        # pack each score box into the frame
        for scoreBox in self._score_boxes:
            self._score_boxes[scoreBox].points_view.grid(row=rw, column=1, sticky=NSEW)
            self._score_boxes[scoreBox].selector.grid(row=rw, column=0, sticky=NSEW)
            rw += 1

    @property
    def selection(self):
        """Get or set the selected score box on the score card.  Pass an empty string to deselect all boxes."""
        return self._assign_selection.get()

    @selection.setter
    def selection(self, box_name):
        self._assign_selection.set(box_name)

    def assign_points(self, box_name, points):
        """
        Update the number of points displayed in a score box on the score card UI

        Parameters:
            box_name (tk str): The name of the box to update the points in
            points (bool): the number of points to place in the score box UI
        """
        self._score_boxes[box_name].points = points

    def box_enabled(self, box_name, enabled):
        """
        Update whether or not a score box on the score card UI can be selected

        Parameters:
            box_name (tk str): The name of the box to disable/enable
            enabled (bool): Whether or not the box can be selected
        """
        self._score_boxes[box_name].enabled = enabled
