import tkinter as tk

from CardSet import CardSet
from WebScraper import WebScraper


class ApplicationManager:
    """This class handles application state and calculations done for cards"""

    def __init__(self):
        # Currently loaded set name
        self._curr_set = None

        # Average prices message
        self._avg_prc_msg = None

        # Currently loaded Card Set
        self._card_set = None

        self._webscraper = WebScraper.get_instance()

    @property
    def curr_set_message(self):
        return "Current Set: {}".format(self._curr_set)

    @property
    def avg_price_msg(self):
        return self._avg_prc_msg

    @property
    def rarities(self):
        return self._card_set.rarities

    def calc_ev(self, rarity_amts):
        """
        Calculates the estimated value(ev) of a booster box given the expected amt of each card rarity per box

        :param rarity_amts: Dict containing the expected amt of each card rarity. Key=rarity, val=amt
        :return: Estimated value in dollars
        """
        total = 0
        for rarity in rarity_amts:
            total += rarity_amts[rarity] * self._card_set.avg_market_price(rarity)
        return total

    def update_current_set(self, event):
        lbox = event.widget
        indxs = lbox.curselection()
        ind = int(indxs[0])
        self._curr_set = lbox.get(ind)
        self._update_card_set(ind, self._curr_set)
        self._update_avg_prc_msg()

    def _update_card_set(self, ind, set_name):
        """
        Updates the member variable _card_set

        :param ind: Index of the selected set
        :param set_name: Name of the selected set
        :return: None
        """
        webscraper = WebScraper.get_instance()
        webscraper.update_page(ind)
        self._card_set = CardSet(set_name, webscraper.get_cards())

    def _update_avg_prc_msg(self):
        """
        Updates the text displayed for this set
        """
        new_msg = []
        for rarity in self._card_set.rarities:
            new_msg.append("Average {} Market Price: {}"
                           .format(rarity, self._card_set.avg_market_price(rarity)))
        self._avg_prc_msg = new_msg
