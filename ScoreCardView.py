from tkinter import *
from tkinter import ttk as tk

yahtzee_gui = Tk()
yahtzee_gui.title('Yahtzee!')


class ScoreBoxView:
    def __init__(self, master, label, can_assign, assignment_var):
        self.frame = tk.Frame(master)
        self.points = Entry(self.frame, width=3, state='disabled')
        if can_assign:
            self.selector = tk.Radiobutton(self.frame, variable=assignment_var, text=label, width=11, value=label)
        else:
            self.selector = tk.Label(self.frame, text=label, width=11)

        self.selector.pack(side=LEFT, expand=True)
        self.points.pack(side=LEFT, expand=True)

    def update_points(self, num_points):
        self.points.insert(0, num_points)

    def enabled(self, enable):
        if enable:
            self.selector.configure(state=NORMAL)
        else:
            self.selector.configure(state=DISABLED)


class SectionLabel:
    def __init__(self, master, label):
        self.frame = tk.Frame(master)
        self.section_label = tk.Label(self.frame, text=label, width=14)
        self.section_label.grid(row=0, column=0)


class ScoreCardView:
    def __init__(self, master):
        self.mainFrame = tk.Frame(master)
        self.mainFrame.pack()
        self.assign_selection = StringVar()
        self.upperSectionLabelView = SectionLabel(self.mainFrame, "UPPER SECTION")
        self.acesView = ScoreBoxView(self.mainFrame, "Aces", True, self.assign_selection)
        self.twosView = ScoreBoxView(self.mainFrame, "Twos", True, self.assign_selection)
        self.threesView = ScoreBoxView(self.mainFrame, "Threes", True, self.assign_selection)
        self.foursView = ScoreBoxView(self.mainFrame, "Fours", True, self.assign_selection)
        self.fivesView = ScoreBoxView(self.mainFrame, "Fives", True, self.assign_selection)
        self.sixesView = ScoreBoxView(self.mainFrame, "Sixes", True, self.assign_selection)
        self.totalScoreView = ScoreBoxView(self.mainFrame, "TOTAL SCORE", False, self.assign_selection)
        self.bonusView = ScoreBoxView(self.mainFrame, "BONUS", False, self.assign_selection)
        self.upper1TotalView = ScoreBoxView(self.mainFrame, "TOTAL", False, self.assign_selection)
        self.lowerSectionLabelView = SectionLabel(self.mainFrame, "LOWER SECTION")
        self.threeOfAKindView = ScoreBoxView(self.mainFrame, "3 of a kind", True, self.assign_selection)
        self.fourOfAKindView = ScoreBoxView(self.mainFrame, "4 of a kind", True, self.assign_selection)
        self.fullHouseView = ScoreBoxView(self.mainFrame, "Full House", True, self.assign_selection)
        self.smallStraightView = ScoreBoxView(self.mainFrame, "Sm. Straight", True, self.assign_selection)
        self.largeStraightView = ScoreBoxView(self.mainFrame, "Lg. Straight", True, self.assign_selection)
        self.yahtzeeView = ScoreBoxView(self.mainFrame, "YAHTZEE", True, self.assign_selection)
        self.chanceView = ScoreBoxView(self.mainFrame, "Chance", True, self.assign_selection)
        self.lowerTotalView = ScoreBoxView(self.mainFrame, "Total (Lower)", False, self.assign_selection)
        self.upper2TotalView = ScoreBoxView(self.mainFrame, "Total (Upper)", False, self.assign_selection)
        self.grandTotalView = ScoreBoxView(self.mainFrame, "GRAND TOTAL", False, self.assign_selection)
        self.scoreBoxes = [
            self.upperSectionLabelView,
            self.acesView,
            self.twosView,
            self.threesView,
            self.foursView,
            self.fivesView,
            self.sixesView,
            self.totalScoreView,
            self.bonusView,
            self.upper1TotalView,
            self.lowerSectionLabelView,
            self.threeOfAKindView,
            self.fourOfAKindView,
            self.fullHouseView,
            self.smallStraightView,
            self.largeStraightView,
            self.yahtzeeView,
            self.yahtzeeView,
            self.chanceView,
            self.lowerTotalView,
            self.upper2TotalView,
            self.grandTotalView
        ]
        rw = 0
        for scoreBox in self.scoreBoxes:
            scoreBox.frame.grid(row=rw, column = 0)
            rw += 1



score = ScoreCardView(yahtzee_gui)


yahtzee_gui.mainloop()
