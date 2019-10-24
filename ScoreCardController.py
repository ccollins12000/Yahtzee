import ScoreCard as SC
import ScoreCardView as SCV


class ScoreBoxController:
    def __init__(self, view, model):
        self.view = SCV.ScoreBoxView()
        self.model = SC.Aces()

    def assign_points(self, dice):
        self.model.assign_points(dice)
        self.view.enabled(not self.model.assigned())
        self.view.update_points(self.model.getpoints())




class ScoreCardController:
    def __init__(self):
        self.scoreCard = SC.ScoreCard()
        self.scoreView = SCV.ScoreCardView()

    def assign_dice(self, dice):
        self.scoreView.get_selection()


SC.Aces()
SCV
SBC = ScoreBoxController()