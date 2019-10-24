class ScoreBox:

    def __init__(self, box_type):
        self.points = 0
        self.assigned = False
        self.name = box_type
        if box_type == 'aces':
            self.assign_points_func = self.aces_calc
        elif box_type == 'twos':
            self.assign_points_func = self.two_calc
        else:
            self.assign_points_func = self.two_calc

    def aces_calc(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(4) * 4
            self.points = points
            self.assigned = True

    def two_calc(self, dice):
        if not self.assigned:
            points = dice.dice_roll_count(2) * 2
            self.points = points
            self.assigned = True



s = ScoreBox(

)

