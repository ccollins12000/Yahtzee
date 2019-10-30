from tkinter import *
import YahtzeeViews
import YahtzeeModel


def empty_function():
    pass


class Yahtzee:
    def __init__(self, tk_master):
        self._view = YahtzeeViews.YahtzeeView(tk_master, self.roll_dice, self.assign_roll ,self.next_turn)
        self._model = YahtzeeModel.YahtzeeModel()
        self.roll_dice()
        self.view_to_model = {
            'Aces': 'Aces', 'Twos': 'Twos', 'Threes': 'Threes', 'Fours': 'Fours', 'Fives': 'Fives', 'Sixes': 'Sixes',
            '3 of a Kind': '3 of a Kind', '4 of a Kind': '4 of a Kind', 'Full House': 'Full House',
            'Small Straight': 'Small Straight', 'Large Straight': 'Large Straight', 'Yahtzee': 'Yahtzee',
            'Chance': 'Chance', 'Bonus': 'Bonus', 'Upper Total': 'Upper Total', 'Lower Total': 'Lower Total',
            'Grand Total': 'Grand Total'
        }
        self._view.rolls_remaining = self._model.rolls_remaining

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

    def update_view(self):
        self.update_score_card()
        self.update_dice()

    def next_turn(self):
        self._model.next_turn()
        self.update_view()

    def roll_dice(self):
        self.update_dice_select()
        self._model.roll_dice()
        self.update_dice()
        self._view.rolls_remaining = self._model.rolls_remaining

    def assign_roll(self):
        box_name = self.view_to_model[self._view.selected_box]
        self._model.assign_roll(box_name)
        self.update_view()


yahtzee_tk = Tk()
y = Yahtzee(yahtzee_tk)
yahtzee_tk.mainloop()
