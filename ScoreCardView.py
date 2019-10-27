from tkinter import *
from tkinter import ttk as tk


class ScoreBoxView:
    """
    This is a class for an individual score box on a Yahtzee score sheet

    Attributes:
        name (str): The name of the score box
        frame (tk.frame): The tk frame object containing the score box UI elements
        points (int): The number of points in the scorebox
        enabled (bool): Whether or not the score box can be selected
    """

    def __init__(self, master, label, can_assign, assignment_var):
        """
        The constructor for ScoreBoxView

        Parameters:
            master (tk object): The tk master object to place the score box UI into
            label (str): The name of the score box, also displays as a text label next to the box on the UI
            can_assign (bool): Whether a dice roll can be assigned to the score box (For Example: the grand total score box should have False passed here)
            assignment_var (tk StringVar): The variable where the selected score box will be stored. Passed from the larger score card view object.
        """
        self._frame = tk.Frame(master)
        self._name = label
        self._points_view = Entry(self.frame, width=3, state='disabled')
        if can_assign:
            self._selector = tk.Radiobutton(self.frame, variable=assignment_var, text=label, width=11, value=label)
        else:
            self._selector = tk.Label(self.frame, text=label, width=11)

        self._selector.pack(side=LEFT, expand=True)
        self._points_view.pack(side=LEFT, expand=True)

    @property
    def points(self):
        """Get or set the points displayed in the score box"""
        return self._points_view.get()

    @points.setter
    def points(self, value):
        self._points_view.configure(state=NORMAL)
        self._points_view.delete(0, END)
        self._points_view.insert(0, value)
        self._points_view.configure(state=DISABLED)

    @property
    def enabled(self):
        """Enabled or disable the score box from being able to be selected for assigning a dice roll"""
        return self._selector.state()

    @enabled.setter
    def enabled(self, enable):
        if enable:
            self._selector.configure(state=NORMAL)
        else:
            self._selector.configure(state=DISABLED)

    @property
    def frame(self):
        """Get the tk frame containing all the score box UI elements"""
        return self._frame

    @property
    def name(self):
        """Get the name of the score box"""
        return self._name


class SectionLabel:
    def __init__(self, master, label):
        self.frame = tk.Frame(master)
        self.name = label
        self.section_label = tk.Label(self.frame, text=label, width=14)
        self.section_label.grid(row=0, column=0)


class ScoreCardView:
    def __init__(self, master, assign_fun):
        boxes = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a Kind', '4 of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance']
        self.scoreBoxes = []
        self.mainFrame = tk.Frame(master)
        self.mainFrame.pack()
        self.assign_selection = StringVar()
        for box in boxes:
            self.scoreBoxes.append(ScoreBoxView(self.mainFrame, box, True, self.assign_selection))
        rw = 0
        for scoreBox in self.scoreBoxes:
            scoreBox.frame.grid(row=rw, column=0)
            rw += 1

        self.btn_assign_roll = tk.Button(master, text="Assign Roll", command=assign_fun)
        self.btn_assign_roll.pack()

    def get_selection(self):
        return self.assign_selection.get()

    def assign_points(self, box_name, points):
        for scoreBox in self.scoreBoxes:
            if box_name == scoreBox.name:
                'assign'
                scoreBox.points = points

    def box_enabled(self, box_name, enabled):
        for scoreBox in self.scoreBoxes:
            if box_name == scoreBox.name:
                scoreBox.enabled = enabled

    def deselect(self):
        self.assign_selection.set('')

