import Tkinter as tk


class Layout():
    def __init__(self, root):
        self.root = root
        self.root.title('Settings')
        root.geometry("400x200")
        # SCALES
        self.threshold = tk.Scale(root, from_=1, to=300, orient="horizontal",
                                  length=200)
        self.erosion = tk.Scale(root, from_=1, to=100, orient="horizontal",
                                length=200)
        self.dilation = tk.Scale(root, from_=1, to=100, orient="horizontal",
                                 length=200)
        self.opening = tk.Scale(root, from_=1, to=100, orient="horizontal",
                                length=200)
        # LABELS
        self.label_threshold = tk.Label(root, text="varThreshold:")
        self.label_erosion = tk.Label(root, text="Erosion:")
        self.label_dilation = tk.Label(root, text="Dilatation:")
        self.label_opening = tk.Label(root, text="Opening:")
        # CHECKBUTTONS
        self.check_erosion = tk.Checkbutton(root, text="ativar",
                                            command=lambda: self.updateList(0))
        self.check_dilation = tk.Checkbutton(root, text="ativar",
                                             command=lambda: self.updateList(1)
                                             )
        self.check_opening = tk.Checkbutton(root, text="ativar",
                                            command=lambda: self.updateList(2))
        # LISTBOX
        self.list = tk.Listbox(root, height=3, width=8)
        # BUTTONS
        self.button_clear = tk.Button(root, text='CLEAR LIST', command=lambda:
                                      self.updateList('clear')
                                      )
        # Show Widgets
        self.label_threshold.grid(row=0, column=0)
        self.threshold.grid(row=0, column=1)
        self.label_erosion.grid(row=1, column=0)
        self.erosion.grid(row=1, column=1)
        self.label_dilation.grid(row=2, column=0)
        self.dilation.grid(row=2, column=1)
        self.label_opening.grid(row=3, column=0)
        self.opening.grid(row=3, column=1)
        self.check_erosion.grid(row=1, column=2, sticky=tk.S)
        self.check_dilation.grid(row=2, column=2, sticky=tk.S)
        self.check_opening.grid(row=3, column=2, sticky=tk.S)
        self.list.grid(row=0, column=4, rowspan=2)
        self.button_clear.grid(row=2, column=4, )

    def updateList(self, id_):
        size = self.list.size()
        if id_ == 0:
            self.list.insert((size+1), 'erosion')
        if id_ == 1:
            self.list.insert((size+1), 'dilation')
        if id_ == 2:
            self.list.insert((size+1), 'opening')
        if id_ is 'clear':
            self.list.delete(0, size)
            self.check_erosion.configure(onvalue=0)
            self.check_dilation.configure(onvalue=0)
            self.check_opening.configure(onvalue=0)

root = tk.Tk()
layout = Layout(root)
root.mainloop()
