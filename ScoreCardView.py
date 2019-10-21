from tkinter import *
from tkinter import ttk as tk

yahtzee_gui = Tk()
yahtzee_gui.title('Yahtzee!')
score_card = tk.Frame(yahtzee_gui)
score_card.pack()
assign_to = StringVar()


class ScoreBoxView:
    def __init__(self, label, can_assign):
        self.frame = tk.Frame(score_card, width=14)
        self.points = Entry(self.frame, width=3, state='disabled')
        if can_assign:
            self.selector = tk.Radiobutton(self.frame, variable=assign_to, text=label, width=11, value=label)
        else:
            self.selector = tk.Label(self.frame, text=label, width=13)

        self.selector.grid(row=0, column=0, sticky=W)
        self.points.grid(row=0, column=1, sticky=E)

    def update_points(self, num_points):
        self.points.insert(0, num_points)

    def enabled(self, enable):
        if enable:
            self.selector.configure(state=NORMAL)
        else:
            self.selector.configure(state=DISABLED)


class SectionLabel:
    def __init__(self, label):
        self.frame = tk.Frame(score_card, width=14)
        self.section_label = tk.Label(self.frame, text=label)
        self.section_label.grid(row=0, column=0)


upperSectionLabel = SectionLabel("UPPER SECTION")
acesView = ScoreBoxView("Aces", True)
twosView = ScoreBoxView("Twos", True)
threesView = ScoreBoxView("Threes", True)
foursView = ScoreBoxView("Fours", True)
fivesView = ScoreBoxView("Fives", True)
sixesView = ScoreBoxView("Sixes", True)
totalScoreView = ScoreBoxView("TOTAL SCORE", False)
bonusView = ScoreBoxView("BONUS", False)
upper1TotalView = ScoreBoxView("TOTAL", False)
lowerSectionLabel = SectionLabel("LOWER SECTION")
threeOfAKindView = ScoreBoxView("3 of a kind", True)
fourOfAKindView = ScoreBoxView("4 of a kind", True)
fullHouseView = ScoreBoxView("Full House", True)
smallStraightView = ScoreBoxView("Sm. Straight", True)
largeStraightView = ScoreBoxView("Lg. Straight", True)
yahtzeeView = ScoreBoxView("YAHTZEE", True)
chanceView = ScoreBoxView("Chance", True)
lowerTotalView = ScoreBoxView("Total (Lower)", False)
upper2TotalView = ScoreBoxView("Total (Upper)", False)
grandTotalView = ScoreBoxView("GRAND TOTAL", False)

points = {
    "UPPER SECTION": upperSectionLabel.frame,
    'Aces': acesView.frame,
    'Twos': twosView.frame,
    "Threes": threesView.frame,
    "Fours": foursView.frame,
    "Fives": fivesView.frame,
    "Sixes": sixesView.frame,
    "TOTAL SCORE": totalScoreView.frame,
    "BONUS": bonusView.frame,
    "TOTAL": upper1TotalView.frame,
    "LOWER SECTION": lowerSectionLabel.frame,
    "3 of a kind": threeOfAKindView.frame,
    "4 of a kind": fourOfAKindView.frame,
    "Full House": fullHouseView.frame,
    "Sm. Straight": smallStraightView.frame,
    "Lg. Straight": largeStraightView.frame,
    "YAHTZEE": yahtzeeView.frame,
    "Chance": chanceView.frame,
    "Total (Lower)": lowerTotalView.frame,
    "Total (Upper)": upper2TotalView.frame,
    "GRAND TOTAL": grandTotalView.frame,
}

rw = 0
for box in points:
    points[box].grid(row=rw, column=0)
    rw = rw + 1


yahtzee_gui.mainloop()
