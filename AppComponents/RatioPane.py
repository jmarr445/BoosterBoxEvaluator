import tkinter as tk


class RatioPane:
    """Displays ratio information for a rarity"""

    def __init__(self, parent, rarity, num_cards_rarity, card_ratio, column):
        """
        Initialize an instance

        :param parent: Parent tk widget
        :param rarity: The rarity for this pane
        :param num_cards_rarity: The number of cards of this rarity in the set
        :param card_ratio: The percentage of the cards of this rarity
        :param column: Which column of the parent to put the gadget in
        """
        self._parent = parent

        # Rarity Tile
        self._frm_tile = tk.Frame(self._parent, borderwidth=2, relief=tk.GROOVE)
        self._frm_tile.grid(column=column, row=0, ipadx=10, ipady=10)
        self._frm_tile.columnconfigure(0, weight=1)
        self._frm_tile.rowconfigure(0, weight=1)
        self._frm_tile.rowconfigure(1, weight=1)
        self._frm_tile.rowconfigure(2, weight=1)

        # Rarity Label
        self._lbl_rarity = tk.Label(self._frm_tile, text=rarity, font=("TKDefaultFont", 10, "bold"), justify=tk.CENTER)
        self._lbl_rarity.grid(column=0, row=0, sticky=(tk.E, tk.W))

        # Total Cards Label
        self._lbl_total_cards = tk.Label(self._frm_tile, text=str(num_cards_rarity) + " Cards", justify=tk.CENTER)
        self._lbl_total_cards.grid(column=0, row=1, sticky=(tk.E, tk.W))

        # Card Ratio Label
        self._lbl_ratio = tk.Label(self._frm_tile, text=str(card_ratio) + "% of set", justify=tk.CENTER)
        self._lbl_ratio.grid(column=0, row=2, sticky=(tk.E, tk.W))