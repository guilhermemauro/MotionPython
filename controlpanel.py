import Tkinter as tk


class Layout():
    def __init__(self, root):
        self.root = root
        self.root.title('Settings')
        self.threshold = tk.Scale(root, from_=1, to=300, orient="horizontal")
        self.erosion = tk.Scale(root, from_=1, to=100, orient="horizontal")
        self.dilation = tk.Scale(root, from_=1, to=100, orient="horizontal")
        self.opening = tk.Scale(root, from_=1, to=100, orient="horizontal")
        self.label_threshold = tk.Label(root, text="varThreshold:")
        self.label_erosion = tk.Label(root, text="Erosion:")
        self.label_dilation = tk.Label(root, text="Dilatation:")
        self.label_opening = tk.Label(root, text="Opening:")
        self.label_threshold.pack()
        self.threshold.pack()
        self.label_erosion.pack()
        self.erosion.pack()
        self.label_dilation.pack()
        self.dilation.pack()
        self.label_opening.pack()
        self.opening.pack()

root = tk.Tk()
layout = Layout(root)
root.mainloop()
