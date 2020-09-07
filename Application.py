import tkinter as tk
from WebScraper import WebScraper


def update_current_set(event):
    lbox = event.widget
    indxs = lbox.curselection()
    ind = int(indxs[0])
    sv_current_set.set("Current Set: {}".format(lbox.get(ind)))
    webScraper.update_page(ind)
    text_info.set(webScraper.set_info)


webScraper = WebScraper()
root = tk.Tk()
root.title("Booster Box Evaluator")
root.minsize(1280, 720)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, minsize=960, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=0)

# The main display window
frm_main = tk.Frame(master=root, width=960, height=720)
frm_main.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S))

# The label for the currently selected set
current_set = ""
sv_current_set = tk.StringVar(value="Current Set: {}".format(current_set))
lbl_current_set = tk.Label(frm_main)
lbl_current_set['textvariable'] = sv_current_set
lbl_current_set.grid(column=0, row=0)

# The label for the selected set information
lbl_set_info = tk.Label(frm_main)
text_info = tk.StringVar(value=webScraper.set_info)
lbl_set_info['textvariable'] = text_info
lbl_set_info.grid(column=0, row=1)

# Configure the set list list box
set_list = tk.StringVar(value=webScraper.get_set_list_names())
set_list_box = tk.Listbox(root, listvariable=set_list, height=10, width=50)
set_list_box.grid(column=1, row=0, sticky=(tk.N, tk.E, tk.W, tk.S))
set_list_box.bind('<<ListboxSelect>>', update_current_set)

# Configure the scroll bar for the set list list box
set_list_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=set_list_box.yview)
set_list_scrollbar.grid(column=2, row=0, sticky=(tk.N, tk.S))
set_list_box['yscrollcommand'] = set_list_scrollbar.set

root.mainloop()
