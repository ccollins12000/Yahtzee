from tkinter import *
from tkinter import ttk as tk

yahtzee_gui = Tk()
yahtzee_gui.title('Yahtzee!')


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
    def __init__(self, master):
        boxes = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a kind', '4 of a kind', 'Full House', 'Sm. Straight', 'Lg. Straight', 'YAHTZEE', 'Chance']
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

        ####To be removed only for testing assign_points method
        self.btn_assign = tk.Button(self.mainFrame, text='Assign Roll', command=self.assign_points)
        self.btn_assign.grid(row=rw, column=0)

    def assign_points(self):
        for scoreBox in self.scoreBoxes:
            if scoreBox.name == self.assign_selection.get():
                scoreBox.update_points(3)
                scoreBox.enabled(False)
                self.assign_selection.set('')


score = ScoreCardView(yahtzee_gui)


yahtzee_gui.mainloop()
