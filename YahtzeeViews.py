from tkinter import *
from tkinter import ttk as tk
import YahtzeeModel

# class PlayerView:
#     def __init__(self, master):
#         player_types = {'Human', 'AI'}
#
#         self._player_type = tk.OptionMenu(master, *player_types)

def empty_function():
    pass

class PlayerView:
    """
    A player picker view
    """
    def __init__(self, master, avatar_file, default_name):
        """
        The constructor function for a player picker view

        :param master: the tk master object
        :param master: the file name of the avatar
        """
        self._tk_master = master
        self.main_frame = tk.Frame(self._tk_master)

        # Avatar Image
        self._avatar_file = avatar_file
        self._image_file = PhotoImage(file=avatar_file)
        self._image = tk.Label(self.main_frame, image=self._image_file)
        self._image.grid(row=0, column=0, columnspan=2)

        # Player Controls
        self._btn_add_remove = tk.Button(self.main_frame, text="  + Add Player  ", command=self.toggle_player)
        self._btn_add_remove.grid(row=1, column=0, sticky=N + S + E + W)
        # Player Type
        OPTIONS = ["Human", "Computer"]
        self._player_type = StringVar()
        self._player_type.set(OPTIONS[0])
        self._cbo_player_type = OptionMenu(self.main_frame, self._player_type, *OPTIONS)
        self._cbo_player_type.grid(row=1, column=1, sticky=N + S + E + W)
        self._lbl_player_name = tk.Label(self.main_frame, text="Player Name: ")
        self._lbl_player_name.grid(row=2, column=0, sticky=N + S + E + W)
        self._txt_player_name = tk.Entry(self.main_frame, width=10, text=default_name)
        self._txt_player_name.grid(row=2, column=1, sticky=N + S + E + W)

        self._added = False

    @property
    def added(self):
        """
        Get whether or not the player has been added to the game
        :return: whether or not the player was added to the game
        """
        return self._added

    @property
    def player_type(self):
        """
        Get whether or not the player is a Human or computer
        :return: whether or not the player is a Human or computer
        """
        return self._player_type.get()

    @property
    def player_name(self):
        return self._txt_player_name.get()

    @property
    def avatar_file(self):
        return self._avatar_file

    def toggle_player(self):
        """
        Add/Remove the player to the game
        :return: None
        """
        if self._added:
            self._added = False
            self._btn_add_remove.configure(text="  + Add Player  ")
        else:
            self._added = True
            self._btn_add_remove.configure(text="- Remove Player")


class PlayersView:
    def __init__(self, master, start_game_function):
        """
        A class object that is a UI for entering all the player names

        :param master: the tk master object that the player entry form is grid into
        :param start_game_function: the function that is executed when the start game button is clicked
        """
        # initialize objects
        master.title('Enter Player Names: ')
        row_count = 6 # all avatar images in directory will get packed into rows and columns
        self.main_frame = tk.Frame(master)
        player_names = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6"]
        self.players = [PlayerView(self.main_frame, "Avatar" + str(index) + ".png", player_names[index]) for index in range(6)]
        for index, player in enumerate(self.players):
            player.main_frame.grid(row=int(index/row_count), column=index%row_count)
        # button for adding players

        self._btn_start_game = tk.Button(self.main_frame, text="Start Game", command=start_game_function)
        self._btn_start_game.grid(row=int(len(self.players)/row_count), column=len(self.players)%row_count, columnspan=row_count - len(self.players)%row_count, stick=N + S + W + E)

        # add first player and pack in frame

    def get_players(self):
        """
        :return: all the players in the game
        """
        all_players = []
        for player in self.players:
            if player.added:
                all_players.append(player)
        return all_players

    def show_view(self):
        """
        Packs the objects into the master TK object
        :return: None
        """
        self.main_frame.pack()

    def hide_view(self):
        """
        Hides the objects into the master TK object
        :return: None
        """
        self.main_frame.pack_forget()


class YahtzeeView:
    """
    This is a class for showing a yahtzee game window

    Parameters:
        master (tkinter master view object): the tkinter master view object or window the yahtzee game will be packed into
        roll_function (function): the function that is run when the roll sdice button is clicked
        assign_function (function): the function that is executed when the assign roll button is clicked
        end_turn_function (function): the function that is executed when the end turn button is cliecked
    """
    def __init__(self, master, roll_function, assign_function, end_turn_function):
        self._player_name = StringVar()

        self._avatar_image = None
        self._avatar_image_box = tk.Label(master, text='Yahtzee')
        self._avatar_image_box.grid(row=0, column=0, rowspan = 2, sticky=N + S + E + W)

        #Dice views
        self._dice_frame = tk.Frame(master)

        self._dice = []
        die_col = 0
        for die_index in range(5):
            self._dice.append(DieView(self._dice_frame, 6))
            self._dice[-1].view.grid(row=0, column=die_col)
            die_col += 1

        self._btn_roll = tk.Button(master, text='Roll Dice', command=roll_function)
        self._dice_frame.grid(row=0, column=1, rowspan=2, sticky=NSEW)
        self._btn_roll.grid(row=0, column=2, sticky=N + S + E + W)

        self._rollsRemainingTxt = StringVar()
        self._rolls_remaining = 0
        self._rollsRemainingTxt.set('Rolls Remaining: ' + str(self._rolls_remaining))
        self._lbl_rolls_remaining = tk.Label(master, textvariable = self._rollsRemainingTxt)
        self._lbl_rolls_remaining.grid(row=1, column=2, sticky=N + S + E + W)

        #Score Card
        self._score_card_frame = tk.Frame(master)
        self._score_card = ScoreCardView(self._score_card_frame)
        self._score_card_frame.grid(row=2, column=0, sticky=W)
        self._btn_assign_roll = tk.Button(master, text="Assign Roll", command=assign_function)
        self._btn_assign_roll.grid(row=3, column=0, sticky=N + S + E + W)
        self._btn_end_turn = tk.Button(master, text="End Turn", command=end_turn_function)
        self._btn_end_turn.grid(row=4, column=0, sticky=N + S + E + W)

        #Game stats/control properties
        self._game_stats_frame = tk.Frame(master)
        self._game_stats_frame.grid(row=2, column=1, rowspan=2, columnspan=2)
        self._can_roll = True
        self._lbl_player_name = tk.Label(self._game_stats_frame, textvariable= self._player_name)
        self._lbl_player_name.grid(row=0,column=0, sticky=N + S + E + W)

    def lock_commands(self):
        self._btn_assign_roll.config(state=DISABLED)
        self._btn_end_turn.config(state=DISABLED)
        self._btn_roll.config(state=DISABLED)

    def unlock_commands(self):
        self._btn_assign_roll.config(state=NORMAL)
        self._btn_end_turn.config(state=NORMAL)
        self._btn_roll.config(state=NORMAL)

    @property
    def player_name(self):
        return self.player_name.get()

    @player_name.setter
    def player_name(self, name):
        self._player_name.set(name + ' may now take their turn.')

    @property
    def avatar_image(self):
        return self._avatar_image

    @avatar_image.setter
    def avatar_image(self, image_file):
        self._avatar_image = PhotoImage(file=image_file)
        self._avatar_image_box.configure(image=self.avatar_image)

    def update_die(self, die_index, value):
        """Update a die at a certain index within the yahtzee game"""
        self._dice[die_index].last_roll = value

    def die_selected(self, die_index):
        """Get whether or not the die at the given index is selected to roll or now"""
        return self._dice[die_index].selected

    def update_box(self, box_name, points, enabled):
        """Update one of the score boxes within the yahtzee game view"""
        self._score_card.assign_points(box_name, points)
        self._score_card.box_enabled(box_name, enabled)

    @property
    def selected_box(self):
        """Get which score box is selected"""
        return self._score_card.selection

    @property
    def rolls_remaining(self):
        """Get or set the number of rolls remaining displayed in the yahtzee game view"""
        return self._rolls_remaining

    @rolls_remaining.setter
    def rolls_remaining(self, value):
        self._rolls_remaining = value
        self._rollsRemainingTxt.set('Rolls Remaining: ' + str(self._rolls_remaining))


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