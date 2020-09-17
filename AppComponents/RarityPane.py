import tkinter as tk


class RarityPane:
    """This class is a tkinter component which displays information for a certain card rarity"""

    def __init__(self, parent, rarity, avg_prc_txt, row):
        """
        Initialize an instance

        :param parent: Parent tk widget
        :param rarity: String with the card rarity
        :param avg_prc_txt: String with the text to display for avg prc info
        """
        self._parent = parent
        self._rarity = rarity

        # Configure frame
        self._frame = tk.Frame(parent)
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)
        self._frame.columnconfigure(2, weight=1)
        self._frame.columnconfigure(3, weight=1)
        self._frame.grid(column=0, row=row, sticky=(tk.W, tk.E))

        # Avg Price label
        self._lbl_avg_prc = tk.Label(self._frame, text=avg_prc_txt, justify="left")
        self._lbl_avg_prc.grid(column=0, row=0, sticky=(tk.W, tk.E))

        # Entry label
        self._lbl_entry = tk.Label(self._frame, text="Cards per box: ", justify="right")
        self._lbl_entry.grid(column=2, row=0, sticky=(tk.W, tk.E))

        # Entry widget
        self._entry_val = tk.StringVar(value="0")
        self._entry = tk.Entry(self._frame, justify="left")
        self._entry["textvariable"] = self._entry_val
        self._entry.grid(column=3, row=0)

    @property
    def entry_val(self):
        return self._entry_val

    @property
    def rarity(self):
        return self._rarity
