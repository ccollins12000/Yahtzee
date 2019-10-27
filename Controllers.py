import ScoreCard as SC
import ScoreCardView as SCV
import Die
import DiceView
from tkinter import *
from tkinter import ttk as tk

yahtzee_gui = Tk()
yahtzee_gui.title('Yahtzee!')


class DiceController:
    def __init__(self, tk_master):
        self.dice = Die.Dice(5)
        self.dice_view = DiceView.DiceView(tk_master, 5, self.roll_dice)

    def roll_dice(self):
        die_index = 0
        for die_view in self.dice_view.dice:
            if die_view.selected.get():
                self.dice.get_die(die_index).roll()
                die_view.update_value(self.dice.get_die(die_index).value)
            die_index += 1


class ScoreCardController:
    def __init__(self, tk_master):
        self.scoreCard = SC.ScoreCard()
        self.master_frame = tk_master
        self.score_frame = tk.Frame(tk_master)
        self.dice_frame = tk.Frame(tk_master)

        self.scoreView = SCV.ScoreCardView(self.score_frame, self.assign_dice)
        self.dice = DiceController(self.dice_frame)

        self.score_frame.grid(row=0, column=0, sticky=NSEW)
        self.dice_frame.grid(row=0, column=1, sticky=NSEW)

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

        self.scoreView.assign_points('Bonus', self.scoreCard.bonus_points)
        self.scoreView.assign_points('Upper Total', self.scoreCard.upper_total_points)
        self.scoreView.assign_points('Lower Total', self.scoreCard.lower_total_points)
        self.scoreView.assign_points('Grand Total', self.scoreCard.total_points)

    def assign_dice(self):
        #add parameter for dice
        dice = Die.Dice(6)
        print(dice)
        selection = self.scoreView.selection
        model_translation = self.view_to_model[selection]

        #Assign in score card
        self.scoreCard.assign_roll(model_translation, dice)

        self.update_score_card()
        self.scoreView.selection = ''


score = ScoreCardController(yahtzee_gui)

yahtzee_gui.mainloop()
