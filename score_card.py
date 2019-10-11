from tkinter import *
from tkinter import ttk as tk

yahtzee_gui = Tk()
score_card = tk.Frame(yahtzee_gui)
score_card.pack()
assign_to = StringVar()


def create_score_box(lbl, can_assign):

    if can_assign:
        selector = tk.Radiobutton(score_card, variable=assign_to, text=lbl, width=17, value=lbl)
    else:
        selector = tk.Label(score_card, text=lbl, width=17)

    return [
            selector,
            Entry(score_card, width=3, state='disabled')
        ]


points = {
    "UPPER SECTION": [tk.Label(score_card, text="UPPER SECTION")],
    'Aces': create_score_box('Aces', True),
    'Twos': create_score_box('Twos', True),
    "Threes": create_score_box('Threes', True),
    "Fours": create_score_box('Fours', True),
    "Fives": create_score_box('Fives', True),
    "Sixes": create_score_box('Sixes', True),
    "TOTAL SCORE": create_score_box('TOTAL SCORE', False),
    "BONUS": create_score_box('BONUS', False),
    "TOTAL": create_score_box('TOTAL', False),
    "LOWER SECTION": [tk.Label(score_card, text="LOWER SECTION")],
    "3 of a kind": create_score_box('3 of a kind', True),
    "4 of a kind": create_score_box('4 of a kind', True),
    "Full House": create_score_box('Full House', True),
    "Sm. Straight": create_score_box('Sm. Straight', True),
    "Lg. Straight": create_score_box('Lg. Straight', True),
    "YAHTZEE": create_score_box('YAHTZEE', True),
    "Chance": create_score_box('Chance', True),
    "Total (Lower)": create_score_box('Total (Lower)', False),
    "Total (Upper)": create_score_box('Total (Upper)', False),
    "GRAND TOTAL": create_score_box('GRAND TOTAL', False),
}

rw = 0
for element in points:
    cl = 0
    for box in points[element]:
        box.grid(row=rw, column=cl, columnspan=(4-len(points[element])))
        cl = cl+1
    rw = rw + 1

yahtzee_gui.mainloop()
