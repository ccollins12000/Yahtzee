"""This module contains code for a player view

"""
from tkinter import *
from tkinter import ttk as tk


class PlayerView:
    """
    A player picker view

    Attributes:
        main_frame (obj): the tkinter frame object that contains the player view
    """
    def __init__(self, master, avatar_file, default_name):
        """The player view constructor

        Note:
            The player view must be manually shown view the main frame attribute

        Args:
            master (obj): The Tkinter master object that contains the player view
            avatar_file (str): The file path to the avatar picture file
            default_name (str): The default name for the player
        """
        self._tk_master = master
        self.main_frame = tk.Frame(self._tk_master)

        # Avatar Image
        self._avatar_file = avatar_file
        self._image_file = PhotoImage(file=avatar_file)
        self._image = tk.Label(self.main_frame, image=self._image_file)
        self._image.grid(row=1, column=0, columnspan=2, sticky=N + S + E + W)

        # Player Controls
        self._btn_add_remove = tk.Button(self.main_frame, text="  + Add Player  ", command=self.toggle_player)
        self._btn_add_remove.grid(row=2, column=0, columnspan=2, sticky=N + S + E + W)
        # Player Type
        OPTIONS = ["Human", "Computer"]
        self._player_type = StringVar()
        self._player_type.set(OPTIONS[0])
        self._cbo_player_type = OptionMenu(self.main_frame, self._player_type, *OPTIONS)
        self._cbo_player_type.grid(row=0, column=0, sticky=N + S + E + W, columnspan=2)
        self._lbl_player_name = tk.Label(self.main_frame, text="Player Name: ")
        self._lbl_player_name.grid(row=3, column=0, sticky=N + S + E + W)
        self._txt_player_name = tk.Entry(self.main_frame, width=10, text=default_name)
        self._txt_player_name.grid(row=3, column=1, sticky=N + S + E + W)
        self._txt_player_name.delete(0, END)
        self._txt_player_name.insert(0, default_name)

        self._added = False

    @property
    def added(self):
        """
        Get whether or not the player has been added to the game
        """
        return self._added

    @property
    def player_type(self):
        """
        Get whether or not the player is a Human or computer
        """
        return self._player_type.get()

    @property
    def player_name(self):
        return self._txt_player_name.get()

    @property
    def avatar_file(self):
        """
        Get the avatar file path
        """
        return self._avatar_file

    def toggle_player(self):
        """
        Add/Remove the player to the game
        """
        if self._added:
            self._added = False
            self._btn_add_remove.configure(text="  + Add Player   ")
        else:
            self._added = True
            self._btn_add_remove.configure(text="- Remove Player")
