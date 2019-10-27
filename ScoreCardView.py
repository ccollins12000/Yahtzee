from tkinter import *
from tkinter import ttk as tk


class ScoreBoxView:
    def __init__(self, master, label, can_assign, assignment_var):
        self.frame = tk.Frame(master)
        self.name = label
        self.points = Entry(self.frame, width=3, state='disabled')
        if can_assign:
            self.selector = tk.Radiobutton(self.frame, variable=assignment_var, text=label, width=11, value=label)
        else:
            self.selector = tk.Label(self.frame, text=label, width=11)

        self.selector.pack(side=LEFT, expand=True)
        self.points.pack(side=LEFT, expand=True)

    def update_points(self, num_points):
        self.points.configure(state=NORMAL)
        self.points.delete(0, END)
        self.points.insert(0, num_points)
        self.points.configure(state=DISABLED)

    def enabled(self, enable):
        if enable:
            self.selector.configure(state=NORMAL)
        else:
            self.selector.configure(state=DISABLED)


class SectionLabel:
    def __init__(self, master, label):
        self.frame = tk.Frame(master)
        self.name = label
        self.section_label = tk.Label(self.frame, text=label, width=14)
        self.section_label.grid(row=0, column=0)


class ScoreCardView:
    def __init__(self, master, assign_fun):
        boxes = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a Kind', '4 of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yahtzee', 'Chance']
        self.scoreBoxes = []
        self.mainFrame = tk.Frame(master)
        self.mainFrame.pack()
        self.assign_selection = StringVar()
        for box in boxes:
            self.scoreBoxes.append(ScoreBoxView(self.mainFrame, box, True, self.assign_selection))
        rw = 0
        for scoreBox in self.scoreBoxes:
            scoreBox.frame.grid(row=rw, column=0)
            rw += 1

        self.btn_assign_roll = tk.Button(master, text="Assign Roll", command=assign_fun)
        self.btn_assign_roll.pack()

    def get_selection(self):
        return self.assign_selection.get()

    def assign_points(self, box_name, points):
        for scoreBox in self.scoreBoxes:
            if box_name == scoreBox.name:
                'assign'
                scoreBox.update_points(points)

    def box_enabled(self, box_name, enabled):
        for scoreBox in self.scoreBoxes:
            if box_name == scoreBox.name:
                scoreBox.enabled(enabled)

    def deselect(self):
        self.assign_selection.set('')

