from tkinter import *
import YahtzeeGameViews
from YahtzeeModel import *
from PlayerModel import *
from Controllers import *
import time
from Bot import *


class Yahtzee:

    def __init__(self, tk_master):
        self._master_tk = tk_master
        # Main views
        self._view = YahtzeeGameViews.YahtzeeView(self._master_tk, self.roll_dice, self.assign_roll, self.next_turn)
        self._end_game_view = YahtzeeGameViews.GameSummary(self._master_tk)
        self._collect_players_view = YahtzeeGameViews.PlayersView(tk_master, self.begin_game)

        # Model
        self._model = YahtzeeModel()

        # Setup Controllers
        self._score_card_controller = CurrentScoreCardController(self._view._score_card, self._model)
        self._player_score_card_controllers = []
        self._dice_controller = DiceController(
            [die_view for die_view in self._view._dice],
            [die for die in self._model._dice]
        )

        # Initialize Game
        self._collect_players_view.show_view()

    def begin_game(self):
        if len(self._collect_players_view.get_players()) > 0:
            self._collect_players_view.main_frame.pack_forget()

            # Build Players
            for player in self._collect_players_view.get_players():
                self._model.add_player(Player(player.player_name, player.avatar_file, player.player_type))
                self._end_game_view.add_player(player.avatar_file, player.player_name)
                self._player_score_card_controllers.append(ScoreCardController(self._end_game_view._players[-1]["Score Card View"], self._model._players[-1].score_card))

            # start game
            self._model.start_game()

            #Update Views
            self._view.show_view()
            self._master_tk.title("Play Yahtzee!")
            self.update_view()
            self.check_take_ai_turn()


    def lock_view(self):
        self._view.lock_commands()

    def unlock_view(self):
        self._view.unlock_commands()

    def check_take_ai_turn(self):
        if self._model.current_player.player_type == 'Computer':
            self._view.lock_commands()
            # must call update before pausing for https://stackoverflow.com/questions/30057844/python-tkinter-time-sleep

            self._view._main_frame.update()
            time.sleep(1)
            # Account for straights
            # Account for full house
            # Account for boxes already assigned
            while self._model.rolls_remaining > 0 and of_a_kind_size(self._model.get_dice()) < 5:
                dice = self._model.get_dice()
                rolls = decide_roll(dice, self._model.current_player.score_card)
                # value_going_for = max(dice, key=dice.count)
                # for die_index, die in enumerate(dice):
                #     self._view.update_die_selected(die_index, not die == value_going_for)
                for die_index, die in enumerate(dice):
                    self._view.update_die_selected(die_index, not rolls[die_index])
                self._view._main_frame.update()
                time.sleep(1)
                self.roll_dice()
                self._view._main_frame.update()
                time.sleep(1)
            box_to_assign = decide_box(self._model.get_dice(), self._model.current_player.score_card)
            # print(self._model.current_player.player_name, ' : ', box_to_assign, ' : ', self._model.get_dice())
            self._model.assign_roll(box_to_assign)

            self._view._main_frame.update()
            self._view.unlock_commands()
            self.next_turn()

    # Action Functions
    def next_turn(self):
        self._model.next_turn()
        #Check if game is over
        if self._model.game_over:
            #Show final game stats
            self._view.hide_view()
            for score_card in self._player_score_card_controllers:
                score_card.update_view()
            self._end_game_view.show_view()
        else:
            # Update View and Pass to Bot if applicable
            self.update_view()  # careful with removing this the model selects all the dice for re-roll when turn ends.
            self.check_take_ai_turn()

    def roll_dice(self):
        # pass the selected dice to the model and roll them
        self._dice_controller.update_dice_select()
        self._model.roll_dice()
        self.update_view()

    def assign_roll(self):
        box_name = view_to_model[self._view.selected_box]
        self._model.assign_roll(box_name)
        self.update_view()

    # Updating view/model functions
    def update_view(self):
        self._score_card_controller.update_view()
        self._dice_controller.update_dice()
        self._view.instructions = self._model.instructions
        self._view.rolls_remaining = self._model.rolls_remaining
        self._dice_controller.update_dice_select() # careful with removing this the model selects all the dice for re-roll when turn ends.
        self._view.avatar_image = self._model.current_player.avatar_file


yahtzee_tk = Tk()
y = Yahtzee(yahtzee_tk)
yahtzee_tk.mainloop()
