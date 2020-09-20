from APICaller import APICaller
from CardSet import CardSet


class ApplicationManager:
    """This class handles application state and calculations done for cards"""

    def __init__(self):
        # Currently loaded set name
        self._curr_set = None

        # Average prices message
        self._avg_prc_msg = None

        # Currently loaded Card Set
        self._card_set = None

        # Use to make tcgplayer api calls
        self._api_caller = APICaller()

        # List of pokemon sets
        self._sets = self._api_caller.get_all_sets()

    @property
    def curr_set_message(self):
        return "Current Set: {}".format(self._curr_set)

    @property
    def avg_price_msg(self):
        return self._avg_prc_msg

    @property
    def rarities(self):
        return self._card_set.rarities

    @property
    def set_names(self):
        return [group["name"] for group in self._sets["results"]]

    def calc_ev(self, rarity_amts):
        """
        Calculates the estimated value(ev) of a booster box given the expected amt of each card rarity per box

        :param rarity_amts: Dict containing the expected amt of each card rarity. Key=rarity, val=amt
        :return: Estimated value in dollars
        """
        total = 0
        for rarity in rarity_amts:
            total += rarity_amts[rarity] * self._card_set.avg_market_price(rarity)
        return round(total, 2)

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
        self._curr_groupID = self._sets["results"][ind]["groupId"]
        self._card_set = CardSet(set_name, self._api_caller.get_cards_for_set(self._curr_groupID),
                                 self._api_caller.get_card_prices(self._curr_groupID))

    def _update_avg_prc_msg(self):
        """
        Updates the text displayed for this set
        """
        new_msg = []
        for rarity in self._card_set.rarities:
            new_msg.append("Average {} Market Price: {}"
                           .format(rarity, self._card_set.avg_market_price(rarity)))
        self._avg_prc_msg = new_msg
