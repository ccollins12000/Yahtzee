import ScoreCard as SC
import ScoreCardView as SCV
import Die
from tkinter import *
from tkinter import ttk as tk

yahtzee_gui = Tk()
yahtzee_gui.title('Yahtzee!')


#class ScoreBoxController:
#    def __init__(self, view, model):
#        self.view = view
#        self.model = SC.Aces()
#
#    def assign_points(self, dice):
#        self.model.assign_points(dice)
#        self.view.enabled(not self.model.assigned())
#        self.view.update_points(self.model.getpoints())


class ScoreCardController:
    def __init__(self, tk_master):
        self.scoreCard = SC.ScoreCard()
        self.scoreView = SCV.ScoreCardView(tk_master, self.assign_dice)
        self.view_to_model = {
            'Aces': 'Aces', 'Twos': 'Twos', 'Threes': 'Threes', 'Fours': 'Fours', 'Fives': 'Fives', 'Sixes': 'Sixes',
            '3 of a Kind': '3 of a Kind', '4 of a Kind': '4 of a Kind', 'Full House': 'Full House',
            'Small Straight': 'Small Straight', 'Large Straight': 'Large Straight', 'Yahtzee': 'Yahtzee',
            'Chance': 'Chance'
        }

    def update_score_card(self):
        for box in self.view_to_model:
            view_name = box
            model_name = self.view_to_model[box]
            if self.scoreCard.get_box_assigned(model_name):
                self.scoreView.assign_points(view_name, self.scoreCard.get_box_points(model_name))
                self.scoreView.box_enabled(view_name, not self.scoreCard.get_box_assigned(model_name))
            else:
                self.scoreView.box_enabled(view_name, not self.scoreCard.get_box_assigned(model_name))

    def assign_dice(self):
        #add parameter for dice
        dice = Die.Dice(6)
        print(dice)
        selection = self.scoreView.get_selection()
        model_translation = self.view_to_model[selection]

        #Assign in score card
        self.scoreCard.assign_roll(model_translation, dice)

        self.update_score_card()
        self.scoreView.deselect()

score = ScoreCardController(yahtzee_gui)

yahtzee_gui.mainloop()
