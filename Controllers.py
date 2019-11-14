"""Controllers

This module contains code for connecting the Yahtzee game logic (model) to the display (view) and updating between the two

Attributes:
    view_to_model (dict):
        A dictionary for translating the name of the score box in the view to the name of the score box in the model
"""

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
    """An object for connecting the logic of the score card to the display

    """
    def __init__(self, view, model):
        """
        The constructor for a score card controller

        Args:
            view (obj): A Yahtzee score card view object
            model (obj): a Yahtzee score card model object
        """
        self._view = view
        self._model = model

    def update_view(self):
        """Updates the view with everything that has happened in the model"""
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
    """Extends the score card controller to have visibility to the yahtzee model.  Specifically for score card view for the current player in game play.

    """
    def __init__(self, view, yahtzee_model):
        """
        The constructor for a current score card controller

        Args:
            view (obj): A Yahtzee score card view object
            yahtzee_model (obj): a Yahtzee Game model object
        """
        super().__init__(view, None)
        self.yahtzee = yahtzee_model


    def update_view(self):
        """Updates the view with everything that has happened in the model"""
        self._model = self.yahtzee.current_player.score_card
        super().update_view()


class DiceController:
    """Connects the dice in the model to the display (view)

    """
    def __init__(self, dice_views, dice_models):
        """
        The constructor for the dice controller

        Args:
            dice_views (obj): A list of dice displays from the Yahtzee view
            dice_models (obj): A list of dice objects from the Yahtzee model
        """
        self._dice_views = dice_views
        self._dice_models = dice_models

    def update_dice_select(self):
        """Passes the user selections on the view to the model"""
        for die_view, die_model in zip(self._dice_views, self._dice_models):
            if die_view.selected == 1:
                view_selected = True
            else:
                view_selected = False
            die_model.selected = view_selected

    def update_dice(self):
        """Updates the yahtzee dice views with the current roll values in the model"""
        for die_view, die_model in zip(self._dice_views, self._dice_models):
            die_view.last_roll = die_model.value

    def update_view(self):
        """Updates the model with the user dice selections in the view and updates the view with the current dice roll values in the model"""
        self.update_dice_select()
        self.update_dice()