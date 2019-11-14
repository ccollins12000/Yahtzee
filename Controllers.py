view_to_model = {
    'Aces': 'Aces',
    'Twos': 'Twos',
    'Threes': 'Threes',
    'Fours': 'Fours',
    'Fives': 'Fives',
    'Sixes': 'Sixes',
    '3 of a Kind': '3 of a Kind',
    '4 of a Kind': '4 of a Kind',
    'Full House': 'Full House',
    'Small Straight': 'Small Straight',
    'Large Straight': 'Large Straight',
    'Yahtzee': 'Yahtzee',
    'Chance': 'Chance',
    'Bonus': 'Bonus',
    'Upper Total': 'Upper Total',
    'Lower Total': 'Lower Total',
    'Grand Total': 'Grand Total'
}


class ScoreCardController(object):
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def update_view(self):
        for box in view_to_model:
            view_name = box
            model_name = view_to_model[box]
            model_points = self._model.get_box_points(model_name)
            model_assigned = self._model.get_box_assigned(model_name)

            if model_assigned:
                self._view.assign_points(view_name, model_points)
                self._view.box_enabled(view_name, not model_assigned)
            else:
                self._view.assign_points(view_name, '')
                self._view.box_enabled(view_name, not model_assigned)


class CurrentScoreCardController(ScoreCardController):
    def __init__(self, view, yahtzee_model):
        super().__init__(view, None)
        self.yahtzee = yahtzee_model


    def update_view(self):
        self._model = self.yahtzee.current_player.score_card
        super().update_view()


class DiceController:
    def __init__(self, dice_views, dice_models):
        self._dice_views = dice_views
        self._dice_models = dice_models

    def update_dice_select(self):
        for die_view, die_model in zip(self._dice_views, self._dice_models):
            if die_view.selected == 1:
                view_selected = True
            else:
                view_selected = False
            die_model.selected = view_selected

    def update_dice(self):
        for die_view, die_model in zip(self._dice_views, self._dice_models):
            die_view.last_roll = die_model.value

    def update_view(self):
        self.update_dice_select()
        self.update_dice()