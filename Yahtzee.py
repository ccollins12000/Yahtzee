from tkinter import *
import YahtzeeGameViews
from YahtzeeModel import *
from PlayerModel import *
from Controllers import *
import time
from Bot import *


class Yahtzee:
    def __init__(self, tk_master):
        self.view_to_model = {
            'Aces': 'Aces', 'Twos': 'Twos', 'Threes': 'Threes', 'Fours': 'Fours', 'Fives': 'Fives', 'Sixes': 'Sixes',
            '3 of a Kind': '3 of a Kind', '4 of a Kind': '4 of a Kind', 'Full House': 'Full House',
            'Small Straight': 'Small Straight', 'Large Straight': 'Large Straight', 'Yahtzee': 'Yahtzee',
            'Chance': 'Chance', 'Bonus': 'Bonus', 'Upper Total': 'Upper Total', 'Lower Total': 'Lower Total',
            'Grand Total': 'Grand Total'
        }
        self.box_values = {
            'Aces': 1,
            'Twos': 2,
            'Threes': 3,
            'Fours': 4,
            'Fives': 5,
            'Sixes': 6
        }
        self._master_tk = tk_master
        # Main views
        self._view = YahtzeeGameViews.YahtzeeView(self._master_tk, self.roll_dice, self.assign_roll, self.next_turn)
        self._end_game_view = YahtzeeGameViews.GameSummary(self._master_tk)
        self._collect_players_view = YahtzeeGameViews.PlayersView(tk_master, self.begin_game)

        # Model
        self._model = YahtzeeModel()

        # Setup Controllers
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
            self._view.show_view()
            self._master_tk.title("Play Yahtzee!")
            self.update_view()
            self.check_take_ai_turn()


    def lock_view(self):
        self._view.lock_commands()

    def unlock_view(self):
        self._view.unlock_commands()

    # AI FUNCTIONS

    def assign_best_score_box(self):
        max_value = -1
        max_score_box = ''

        for score_box in YahtzeeModel.assign_function_lookup.keys():
            current_value = YahtzeeModel.assign_function_lookup[score_box](self._model.get_dice())
            current_box = score_box
            if current_value > max_value and not self._model.current_player.score_card.get_box_assigned(score_box):
                max_value = current_value
                max_score_box = current_box

        self._model.assign_roll(max_score_box)
        self.update_view()

    def get_values_not_achieved(self):
        values_needed = []
        for box in self.box_values:
            if not self._model.current_player.score_card.get_box_assigned(box):
                values_needed.append(self.box_values[box])
        return values_needed

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
            self._model.assign_roll(box_to_assign)
            print(self._model.current_player.player_name,' : ', box_to_assign, ' : ', self._model.get_dice())
            self._view._main_frame.update()
            self._view.unlock_commands()
            self.next_turn()

    # Action Functions
    def next_turn(self):
        self._model.next_turn()
        if self._model.game_over:
            self._view.hide_view()
            for score_card in self._player_score_card_controllers:
                score_card.update_view()
            self._end_game_view.show_view()
        else:
            self.update_view()  # careful with removing this the model selects all the dice for re-roll when turn ends.
            self.check_take_ai_turn()

    def roll_dice(self):
        self._dice_controller.update_dice_select()
        self._model.roll_dice()
        self.update_view()

    def assign_roll(self):
        box_name = self.view_to_model[self._view.selected_box]
        self._model.assign_roll(box_name)
        self.update_view()

    # Updating view/model functions
    def update_view(self):
        self._score_card_controller = ScoreCardController(self._view._score_card, self._model.current_player.score_card)
        self._score_card_controller.update_view()
        self._dice_controller.update_dice()
        self._view.player_name = self._model.current_player.player_name
        self._view.rolls_remaining = self._model.rolls_remaining
        self._dice_controller.update_dice_select() # careful with removing this the model selects all the dice for re-roll when turn ends.
        self._view.avatar_image = self._model.current_player.avatar_file


yahtzee_tk = Tk()
y = Yahtzee(yahtzee_tk)
yahtzee_tk.mainloop()
