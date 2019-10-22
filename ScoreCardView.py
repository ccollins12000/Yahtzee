from tkinter import *
from tkinter import ttk as tk

yahtzee_gui = Tk()
yahtzee_gui.title('Yahtzee!')
score_card = tk.Frame(yahtzee_gui)
score_card.pack()
assign_to = StringVar()


class ScoreBoxView:
    def __init__(self, master, label, can_assign):
        self.frame = tk.Frame(master)
        self.points = Entry(self.frame, width=3, state='disabled')
        if can_assign:
            self.selector = tk.Radiobutton(self.frame, variable=assign_to, text=label, width=11, value=label)
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
    def __init__(self):
        self.text = 0


upperSectionLabel = SectionLabel(score_card, "UPPER SECTION")
acesView = ScoreBoxView(score_card, "Aces", True)
twosView = ScoreBoxView(score_card, "Twos", True)
threesView = ScoreBoxView(score_card, "Threes", True)
foursView = ScoreBoxView(score_card, "Fours", True)
fivesView = ScoreBoxView(score_card, "Fives", True)
sixesView = ScoreBoxView(score_card, "Sixes", True)
totalScoreView = ScoreBoxView(score_card, "TOTAL SCORE", False)
bonusView = ScoreBoxView(score_card, "BONUS", False)
upper1TotalView = ScoreBoxView(score_card, "TOTAL", False)
lowerSectionLabel = SectionLabel(score_card, "LOWER SECTION")
threeOfAKindView = ScoreBoxView(score_card, "3 of a kind", True)
fourOfAKindView = ScoreBoxView(score_card, "4 of a kind", True)
fullHouseView = ScoreBoxView(score_card, "Full House", True)
smallStraightView = ScoreBoxView(score_card, "Sm. Straight", True)
largeStraightView = ScoreBoxView(score_card, "Lg. Straight", True)
yahtzeeView = ScoreBoxView(score_card, "YAHTZEE", True)
chanceView = ScoreBoxView(score_card, "Chance", True)
lowerTotalView = ScoreBoxView(score_card, "Total (Lower)", False)
upper2TotalView = ScoreBoxView(score_card, "Total (Upper)", False)
grandTotalView = ScoreBoxView(score_card, "GRAND TOTAL", False)

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
    #points[box].grid(row=rw, column=0)
    points[box].pack(side=TOP, expand=True)
    rw = rw + 1


yahtzee_gui.mainloop()
