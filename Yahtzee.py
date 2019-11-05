from tkinter import *
import YahtzeeViews
import YahtzeeModel


class Yahtzee:
    def __init__(self, tk_master):
        self.view_to_model = {
            'Aces': 'Aces', 'Twos': 'Twos', 'Threes': 'Threes', 'Fours': 'Fours', 'Fives': 'Fives', 'Sixes': 'Sixes',
            '3 of a Kind': '3 of a Kind', '4 of a Kind': '4 of a Kind', 'Full House': 'Full House',
            'Small Straight': 'Small Straight', 'Large Straight': 'Large Straight', 'Yahtzee': 'Yahtzee',
            'Chance': 'Chance', 'Bonus': 'Bonus', 'Upper Total': 'Upper Total', 'Lower Total': 'Lower Total',
            'Grand Total': 'Grand Total'
        }
        self._master_tk = tk_master
        self._view = None
        self._model = None
        self._collect_players_view = YahtzeeViews.PlayersView(tk_master, self.begin_game)
        self._collect_players_view.show_view()

    def begin_game(self):
        player_names = []
        avatar_files = []
        player_types = []
        player_names.extend(self._collect_players_view.get_player_names())
        avatar_files.extend(self._collect_players_view.get_avatar_files())
        player_types.extend(self._collect_players_view.get_player_types())

        self._collect_players_view.main_frame.pack_forget()

        self._model = YahtzeeModel.YahtzeeModel(player_names, avatar_files, player_types)
        self._view = YahtzeeViews.YahtzeeView(self._master_tk, self.roll_dice, self.assign_roll, self.next_turn)
        self._master_tk.title("Play Yahtzee!")
        self.roll_dice()
        self.update_view()

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
            if current_value > max_value and not self._model.score_card.get_box_assigned(score_box):
                max_value = current_value
                max_score_box = current_box

        self._model.assign_roll(max_score_box)
        self.update_view()

    # Action Functions
    def next_turn(self):
        self._model.next_turn()
        self.update_view() # careful with removing this the model selects all the dice for re-roll when turn ends.
        #doesn't work if first player is computer
        # print(self._model.current_player_type)
        print(self._model.current_player_type)
        if self._model.current_player_type == 'Computer':
            self._view.lock_commands()
            self.assign_best_score_box()
            self._view.unlock_commands()


    def roll_dice(self):
        self.update_dice_select()
        self._model.roll_dice()
        self.update_view()

    def assign_roll(self):
        box_name = self.view_to_model[self._view.selected_box]
        self._model.assign_roll(box_name)
        self.update_view()

    # Updating view/model functions
    def update_view(self):
        self.update_score_card()
        self.update_dice()
        self._view.player_name = self._model.current_player
        self._view.rolls_remaining = self._model.rolls_remaining
        self.update_dice_select() # careful with removing this the model selects all the dice for re-roll when turn ends.
        self._view.avatar_image = self._model.current_avatar

    def update_dice_select(self):
        for die_index in range(5):
            if self._view.die_selected(die_index) == 1:
                view_selected = True
            else:
                view_selected = False
            self._model.toggle_die_for_roll(die_index, view_selected)

    def update_score_card(self):
        for box in self.view_to_model:
            view_name = box
            model_name = self.view_to_model[box]
            model_points = self._model.score_card.get_box_points(model_name)
            model_assigned = self._model.score_card.get_box_assigned(model_name)

            if model_assigned:
                self._view.update_box(view_name, model_points, not model_assigned)
            else:
                self._view.update_box(view_name, '', not model_assigned)

    def update_dice(self):
        dice_values = self._model.get_dice()
        for die_index, die_value in enumerate(dice_values):
            self._view.update_die(die_index, die_value)





yahtzee_tk = Tk()
y = Yahtzee(yahtzee_tk)
yahtzee_tk.mainloop()
