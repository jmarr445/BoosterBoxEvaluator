import tkinter as tk
from WebScraper import WebScraper

webScraper = WebScraper()
window = tk.Tk()
window.title("Booster Box Evaluator")

set_list = tk.StringVar(value=webScraper.get_set_list_names())
set_list_box = tk.Listbox(window, listvariable=set_list, height=10)
set_list_box.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S))


set_list_scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=set_list_box.yview)
set_list_scrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S))

set_list_box['yscrollcommand'] = set_list_scrollbar.set

window.mainloop()