import tkinter as tk

from AppComponents.RarityPane import RarityPane
from ApplicationManager import ApplicationManager
from WebScraper import WebScraper


class MainView:
    """View Class"""

    default_box_prc_msg = "Expected Value: "

    def __init__(self, controller, root):
        """Initialize the components of the app"""
        self.controller = controller

        self.root = root

        # Contains active RarityPane instances
        self._avg_price_msg_list = []

        # Text Variable Initialization
        self._curr_set_msg = tk.StringVar(value="Current Set: ")
        self._box_prc_msg = tk.StringVar(value=self.default_box_prc_msg)

        # Main frame
        self.root.rowconfigure(0, minsize=720, weight=1)
        self.root.columnconfigure(0, minsize=960, weight=1)
        self.root.columnconfigure(1, weight=0)
        self.root.columnconfigure(2, weight=0)

        # Set information display frame
        self.frm_main = None
        self.lbl_current_set = None
        self.calculate_button = None
        self.total_value = None
        self.lbl_total_val = None
        self._lbl_box_price = None
        self.create_frm_main()

        # Configure the set list list box
        self.set_list = tk.StringVar(value=self.controller.get_set_list_names())
        self.set_list_box = tk.Listbox(self.root, listvariable=self.set_list, height=10, width=50)
        self.set_list_box.grid(column=1, row=0, sticky=(tk.N, tk.E, tk.W, tk.S))
        self.set_list_box.bind('<<ListboxSelect>>', self.controller.update_current_set)

        # Configure the scroll bar for the set list list box
        self.set_list_scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.set_list_box.yview)
        self.set_list_scrollbar.grid(column=2, row=0, sticky=(tk.N, tk.E, tk.S))
        self.set_list_box['yscrollcommand'] = self.set_list_scrollbar.set

    @property
    def avg_prc_msg(self):
        return self._avg_price_msg

    @avg_prc_msg.setter
    def avg_prc_msg(self, value):
        self._avg_price_msg.set(value)

    @property
    def box_prc_msg(self):
        return self._box_prc_msg

    @box_prc_msg.setter
    def box_prc_msg(self, val):
        self._box_prc_msg.set(self.default_box_prc_msg+val)

    @property
    def curr_set_msg(self):
        return self._curr_set_msg

    @curr_set_msg.setter
    def curr_set_msg(self, value):
        self._curr_set_msg.set(value)

    @property
    def rarity_amts(self):
        vals = {}
        for pane in self._avg_price_msg_list:
            vals[pane.rarity] = int(pane.entry_val.get())
        return vals

    def update_set_info(self, rarities, messages):
        """Creates widgets to display set info"""
        self._avg_price_msg_list = []

        for idx, msg in enumerate(messages):
            # idx + 1 because the curr set label takes up row 0
            self._avg_price_msg_list.append(RarityPane(self.frm_main, rarities[idx], msg, idx + 1))

        # Create the calculate button
        self.calculate_button = tk.Button(self.frm_main, text="Calculate", command=self.controller.calculate_price)
        self.calculate_button.grid(column=0, row=len(messages) + 1)

    def clear_set_info(self):
        """Prepares app for new set"""
        # Destroy widgets for previous set
        self.frm_main.destroy()
        self.create_frm_main()

        self._box_prc_msg.set(self.default_box_prc_msg)

    def create_frm_main(self):
        """Creates the frm_main property when it does not exist yet"""
        # Set information display frame
        self.frm_main = tk.Frame(master=self.root, width=960, height=720)
        self.frm_main.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S))
        self.frm_main.columnconfigure(0, weight=1)
        self.frm_main.columnconfigure(1, weight=1)

        # The label for the currently selected set
        self.lbl_current_set = tk.Label(self.frm_main, justify="center")
        self.lbl_current_set['textvariable'] = self._curr_set_msg
        self.lbl_current_set.grid(column=0, row=0, sticky=(tk.W, tk.E))

        # The label for the total price
        self._lbl_box_price = tk.Label(self.frm_main, justify="center")
        self.lbl_current_set['textvariable'] = self._box_prc_msg
        self.lbl_current_set.grid(column=1, row=0, sticky=(tk.W, tk.E))
