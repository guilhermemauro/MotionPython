import Tkinter as tk
import numpy as np
import cv2
from multiprocessing import Process

# Window constructor


class Layout():
    def __init__(self, root):
        self.root = root
        self.root.title('Settings')
        root.geometry("463x200")
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
        self.check_erosion = tk.Checkbutton(root, text="activate",
                                            command=lambda: self.updateList(0))
        self.check_dilation = tk.Checkbutton(root, text="activate",
                                             command=lambda: self.updateList(1)
                                             )
        self.check_opening = tk.Checkbutton(root, text="activate",
                                            command=lambda: self.updateList(2))
        # LISTBOX
        self.list = tk.Listbox(root, height=3, width=8)
        # BUTTONS
        self.button_clear = tk.Button(root, text='CLEAR LIST', command=lambda:
                                      self.updateList('clear')
                                      )
        self.button_start = tk.Button(root, text="START",
                                      command=lambda: self.executeBS())
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
        self.button_clear.grid(row=2, column=4)
        self.button_start.grid(row=3, column=4)

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
            self.check_erosion.deselect()
            self.check_dilation.deselect()
            self.check_opening.deselect()

    def executeBS(self):
        # get list order and yours respectives values
        size = self.list.size()
        self.array_keys = self.list.get(0, size)
        self.array_values = []
        for tratament in self.array_keys:
            if tratament == 'erosion':
                self.array_values.append(self.erosion.get())
            if tratament == 'dilation':
                self.array_values.append(self.dilation.get())
            if tratament == 'opening':
                self.array_values.append(self.opening.get())
        self.process = Process(target=self.bsFunction)
        self.process.start()

    def bsFunction(self):
        # read video
        cap = cv2.VideoCapture('sample.mp4')
        # make background subtraction class
        fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=
                                                  self.threshold.get(),
                                                  detectShadows=False)
        # kernel for use in tecniques
        kernel = np.ones((5, 5), np.uint8)
        ret, frame = cap.read()
        while ret:
            # capture dimensions of the video
            # dimensions = frame.shape
            fgmask = fgbg.apply(frame)
            # apply tecniques by order
            for tecnique, value in zip(self.array_keys, self.array_values):
                if tecnique == 'erosion':
                    fgmask = cv2.erode(fgmask, kernel,
                                       iterations=int(value))
                if tecnique == 'opening':
                    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel,
                                              iterations=int(value))
                if tecnique == 'dilation':
                    fgmask = cv2.dilate(fgmask, kernel, iterations=int(value))

#                img, cont, hier = cv2.findContours(fgmask, cv2.RETR_EXTERNAL,
#                                                   cv2.CHAIN_APPROX_NONE)
#                if len(cont) > 0:
#                    for quad in cont:
#                       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2
#                                      )
            cv2.imshow('Background', fgmask)
            # cv2.imshow('original', frame)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
            ret, frame = cap.read()
        cap.release()
        cv2.destroyAllWindows()

root = tk.Tk()
layout = Layout(root)
root.mainloop()
