import tkinter as tk

from Controller import Controller

root = tk.Tk()
root.title("Booster Box Evaluator")
root.minsize(1280, 720)
controller = Controller(root)
root.mainloop()
