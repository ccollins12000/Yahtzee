from tkinter import *
from tkinter import ttk as tk


def empty_function():
    pass


class YahtzeeView:
    def __init__(self, master, roll_function, assign_function, end_turn_function):
        self._game_logo_frame = tk.Button(master, text='Yahtzee')
        self._game_logo_frame.grid(row=0, column=0, sticky=N + S + E + W)

        #Dice views
        self._dice_frame = tk.Frame(master)

        self._dice = []
        die_col = 0
        for die_index in range(5):
            self._dice.append(DieView(self._dice_frame, 6))
            self._dice[-1].view.grid(row=0, column =die_col)
            die_col += 1

        self.btn_roll = tk.Button(master, text="Roll Dice", command=roll_function)
        self._dice_frame.grid(row=0, column=1, sticky=NSEW)
        self.btn_roll.grid(row=0, column=2, sticky=N + S + E + W)

        #Score Card
        self._score_card_frame = tk.Frame(master)
        self._score_card = ScoreCardView(self._score_card_frame)
        self._score_card_frame.grid(row=1, column=0, sticky=W)
        self.btn_assign_roll = tk.Button(master, text="Assign Roll", command=assign_function)
        self.btn_assign_roll.grid(row=2, column=0, sticky=N + S + E + W)
        self.btn_end_turn = tk.Button(master, text="End Turn", command=end_turn_function)
        self.btn_end_turn.grid(row=3, column=0, sticky=N + S + E + W)

        #Game stats/control properties
        self._game_stats_frame = tk.Frame(master)
        self._game_stats_frame.grid(row=1, column=1, rowspan=2, columnspan=2)
        self._rollsRemainingTxt = StringVar()
        self._rolls_remaining = 0
        self._rollsRemainingTxt.set('Rolls Remaining: ' + str(self._rolls_remaining))
        self._can_roll = True

    def update_die(self, die_index, value):
        self._dice[die_index].last_roll = value

    def die_selected(self, die_index):
        return self._dice[die_index].selected

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


class DieView:
    """
    This is a class to display a single die that can be selected

    Attributes:
        selected (bool): Whether or not the die is selected
        last_roll (int): The number diplayed on the die

    """
    def __init__(self, master, initial_roll=None):
        self._last_roll = 6
        if initial_roll is None:
            self._last_roll = 6
        self._image = PhotoImage(file="Die" + str(self._last_roll) + ".png")
        self._selected = IntVar(value=1)
        self.view = tk.Checkbutton(master, image=self._image, variable=self._selected)

    @property
    def selected(self):
        """Get or set whether the die is selected. Toggles the checkbox control"""
        return self._selected.get()

    @selected.setter
    def selected(self, is_selected):
        self._selected.set(is_selected)

    @property
    def last_roll(self):
        """Get or set the number displayed on the die"""
        return self._last_roll

    @last_roll.setter
    def last_roll(self, value):
        if 1 <= value <= 6:
            self._last_roll = value
            self._image = PhotoImage(file="Die" + str(value) + ".png")
            self.view.configure(image=self._image)
        else:
            raise Exception('Value of die view must be between 1 and 6')


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
        self.points_view = tk.Entry(master, width=3, state='disabled')
        if can_assign:
            self.selector = tk.Radiobutton(master, variable=assignment_var, text=name, width=11, value=name)
        else:
            self.selector = tk.Label(master, text=name, width=13)

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
        self.assign_selection = StringVar()

        self.scoreBoxes = {}
        for box_setup in box_setup_instructions:
            assignable = box_setup_instructions[box_setup]['Can Assign']
            self.scoreBoxes[box_setup] = ScoreBoxView(self.mainFrame, box_setup, assignable, self.assign_selection)
        rw = 0
        for scoreBox in self.scoreBoxes:
            self.scoreBoxes[scoreBox].points_view.grid(row=rw, column=1, sticky=NSEW)
            self.scoreBoxes[scoreBox].selector.grid(row=rw, column=0, sticky=NSEW)
            rw += 1

        # Setup button for assigning roll

    @property
    def selection(self):
        """Get or set the selected score box on the score card.  Pass an empty string to deselect all boxes."""
        return self.assign_selection.get()

    @selection.setter
    def selection(self, box_name):
        self.assign_selection.set(box_name)

    def assign_points(self, box_name, points):
        """
        Update the number of points displayed in a score box on the score card UI

        Parameters:
            box_name (tk str): The name of the box to update the points in
            points (bool): the number of points to place in the score box UI
        """
        self.scoreBoxes[box_name].points = points

    def box_enabled(self, box_name, enabled):
        """
        Update whether or not a score box on the score card UI can be selected

        Parameters:
            box_name (tk str): The name of the box to disable/enable
            enabled (bool): Whether or not the box can be selected
        """
        self.scoreBoxes[box_name].enabled = enabled