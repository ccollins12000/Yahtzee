"""This module contains the main windows displayed while initializing and playing a Yahtzee game

"""


from tkinter import *
from tkinter import ttk as tk
from ScoreCardView import *
from PlayerView import *
from DieView import *


class GameSummary:
    """
    This is a class for displaying the results of the game
    """
    def __init__(self, master):
        """
        The constructor for ScoreBoxView

        Notes:
            Players must be added to the view throw the add player method.
            Show view must be called to display the window

        Args:
            master (:obj:): The master tk window the view is displayed into
        """
        self._tk_master = master
        self._main_frame = tk.Frame(self._tk_master)
        self._players = []
        self._images = []
        self._avatar_images = []
        self._player_names = []
        self._score_cards = []

    def add_player(self, avatar_file, player_name):
        """
        Adds players to the view

        Args:
            avatar_file (str:): The path to the avatar file
            player_name (str:) The name of the player
        """
        self._images.append(PhotoImage(file=avatar_file))
        score_frame = tk.Frame(self._main_frame)
        self._players.append(
            {
                "Name": tk.Label(self._main_frame, text=player_name),
                "Image": tk.Label(self._main_frame, image=self._images[-1]),
                "Score Card Frame": score_frame,
                "Score Card View": ScoreCardView(score_frame)
             }
        )
        player = self._players[-1]
        player_index = len(self._players) - 1
        player["Name"].grid(row=0, column=player_index, sticky=N + S + E + W)
        player["Image"].grid(row=1, column=player_index, sticky=N + S + E + W)
        player["Score Card Frame"].grid(row=2, column=player_index, sticky=N + S + E + W)

    def show_view(self):
        """Shows the view in the main tk window"""
        self._main_frame.pack()

    def hide_view(self):
        """Hides the view in the main tk window"""
        self._main_frame.pack_forget()


class PlayersView:
    """
    A class object that is a UI for entering all the player names

    Attributes:
        players (str): All the player views
        main_frame (obj): The main tk window the view is displayed into
    """
    def __init__(self, master, start_game_function):
        """
        The constructor for the players view

        Args:
            master (obj): the tk master object that the player entry form is grid into
            start_game_function (function) : the function that is executed when the start game button is clicked
        """
        # initialize objects
        master.title('Enter Player Names: ')
        row_count = 6 # all avatar images in directory will get packed into rows and columns
        self.main_frame = tk.Frame(master)
        player_names = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6"]
        self.players = [PlayerView(self.main_frame, "avatar_images/Avatar" + str(index) + ".png", player_names[index]) for index in range(6)]
        for index, player in enumerate(self.players):
            player.main_frame.grid(row=int(index/row_count), column=index%row_count)
        # button for adding players

        self._btn_start_game = tk.Button(self.main_frame, text="Start Game", command=start_game_function)
        self._btn_start_game.grid(row=int(len(self.players)/row_count), column=len(self.players)%row_count, columnspan=row_count - len(self.players)%row_count, stick=N + S + W + E)

        # add first player and pack in frame

    def get_players(self):
        """
        obj: Gets all the player views for the added players in the game
        """
        all_players = []
        for player in self.players:
            if player.added:
                all_players.append(player)
        return all_players

    def show_view(self):
        """
        Packs the objects into the master TK object
        """
        self.main_frame.pack()

    def hide_view(self):
        """
        Hides the objects into the master TK object
        """
        self.main_frame.pack_forget()


class YahtzeeView:
    """
    This is a class for showing a yahtzee game window
    """
    def __init__(self, tk_master, roll_function, assign_function, end_turn_function):
        """
        The constructor for yahtzee game play view

        Args:
            tk_master (obj): the tkinter master view object or window the yahtzee game will be packed into
            roll_function (obj): the function that is run when the roll sdice button is clicked
            assign_function (obj): the function that is executed when the assign roll button is clicked
            end_turn_function (obj): the function that is executed when the end turn button is clicked
        """

        self._main_frame = tk.Frame(tk_master)
        master = self._main_frame

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
        self._player_name = StringVar()
        #self._lbl_player_name = tk.Label(self._game_stats_frame, textvariable= self._player_name)
        #self._lbl_player_name.grid(row=0,column=0, sticky=N + S + E + W)

        self._instructions = StringVar()
        self._lbl_instructions = tk.Label(self._game_stats_frame, textvariable= self._instructions)
        self._lbl_instructions.grid(row=0, column=0, sticky=N + S + E + W)

    def lock_commands(self):
        """Disables the command buttons from being able to be clicked"""
        self._btn_assign_roll.config(state=DISABLED)
        self._btn_end_turn.config(state=DISABLED)
        self._btn_roll.config(state=DISABLED)

    def unlock_commands(self):
        """Enables the command buttons so they can be clicked"""
        self._btn_assign_roll.config(state=NORMAL)
        self._btn_end_turn.config(state=NORMAL)
        self._btn_roll.config(state=NORMAL)

    @property
    def instructions(self):
        """str: The instructions displayed on the game view"""
        return self._instructions.get()

    @instructions.setter
    def instructions(self, value):
        self._instructions.set(value)

    @property
    def player_name(self):
        """str: The name of the current player"""
        return self.player_name.get()

    @player_name.setter
    def player_name(self, name):
        self._player_name.set(name + ' may now take their turn.')

    @property
    def avatar_image(self):
        """str: The file path to the avatar file of the current player"""
        return self._avatar_image

    @avatar_image.setter
    def avatar_image(self, image_file):
        self._avatar_image = PhotoImage(file=image_file)
        self._avatar_image_box.configure(image=self.avatar_image)

    def update_die(self, die_index, value):
        """
        Update the value displayed on a die at a given index in the game view

        Args:
            die_index (int): The index of the die to update
            value (int): The value to display on the die
        """
        self._dice[die_index].last_roll = value

    def die_selected(self, die_index):
        """
        Get whether or not a die is selected

        Args:
            die_index (int): The index of the die to retrieve the selected status
        """
        return self._dice[die_index].selected

    def update_die_selected(self, die_index, selected):
        """
        Update whether or not a die is selected

        Args:
            die_index (int): The index of the die to update
            selected (bool): Whether or not the die is selected
        """
        self._dice[die_index].selected = selected

    def update_box(self, box_name, points, enabled):
        """
        Update a box on the score card (points/enabled) given a certain box nam e

        Args:
            box_name (str): The name of the box to update
            points (int): The number of points to display in the box
            enabled (bool): Whether or not the box can be selected/is enabled
        """
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

    def show_view(self):
        """
        Packs the objects into the master TK object
        """
        self._main_frame.pack()

    def hide_view(self):
        """
        Hides the objects into the master TK object
        """
        self._main_frame.pack_forget()


def main():
    """Preview of the Game Views"""
    yahtzee_tk = Tk()
    y = GameSummary(yahtzee_tk)
    y.add_player("avatar_images/Avatar0.png", "Player1")
    y.add_player("avatar_images/Avatar1.png", "Player2")
    y.add_player("avatar_images/Avatar2.png", "Player3")
    y.add_player("avatar_images/Avatar3.png", "Player4")
    y.show_view()
    yahtzee_tk.mainloop()

if __name__ == "__main__":
    main()