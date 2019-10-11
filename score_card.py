from tkinter import *
from tkinter import ttk as tk

score_card = Tk()

assign_to = StringVar()


def create_score_box(lbl):
    return [
            tk.Radiobutton(score_card, variable=assign_to, text=lbl, width=14, value=lbl),
            Entry(score_card, width=3),
            Entry(score_card, width=3)
        ]



points = {
    "UPPER SECTION": [Label(score_card, text="UPPER SECTION")],
    'Aces': create_score_box('Aces'),
    'Twos': create_score_box('Twos'),
    "Threes": create_score_box('Threes'),
    "Fours": create_score_box('Fours'),
    "Fives": create_score_box('Fives'),
    "Sixes": create_score_box('Sixes'),
    "TOTAL SCORE": create_score_box('TOTAL SCORE'),
    "BONUS": create_score_box('BONUS'),
    "TOTAL": create_score_box('TOTAL'),
    "LOWER SECTION": [Label(score_card, text="LOWER SECTION")],
    "3 of a kind": create_score_box('3 of a kind'),
    "4 of a kind": create_score_box('4 of a kind'),
    "Full House": create_score_box('Full House'),
    "Sm. Straight": create_score_box('Sm. Straight'),
    "Lg. Straight": create_score_box('Lg. Straight'),
    "YAHTZEE": create_score_box('YAHTZEE'),
    "Chance": create_score_box('Chance'),
    "Total (Lower)": create_score_box('Total (Lower)'),
    "Total (Upper)": create_score_box('Total (Upper)'),
    "GRAND TOTAL": create_score_box('GRAND TOTAL'),
}

rw = 0
for element in points:
    cl = 0
    for box in points[element]:
        box.grid(row=rw, column=cl, columnspan=(4-len(points[element])))
        cl = cl+1
    rw = rw + 1

score_card.mainloop()
