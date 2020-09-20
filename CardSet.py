import logging


class CardSet:
    """
    This class houses the main logic for calculating statistics for a card set
    """

    def __init__(self, set_name, card_list, card_prices):
        """
        Initialize a CardSet

        :param set_name: String with the name of the card set
        :param card_list: A list of Card objects
        """
        self._set_name = set_name
        self._card_list = card_list
        self._card_prices = card_prices["results"]
        self._rarities = []
        # Make a list of all rarities in the set
        for card in card_list:
            curr_rarity = card["extendedData"][1]["value"]
            if curr_rarity not in self._rarities:
                self._rarities.append(curr_rarity)
        # Calculate the avg market val of each rarity
        self._avg_prices = {}
        for rarity in self._rarities:
            self._avg_prices[rarity] = self._calc_avg_market_price(rarity)

    def avg_market_price(self, rarity):
        """
        Returns stored value of avg market price for given rarity

        :param rarity: String with a rarity that matches the Card objects
        :return: Double with the average market price
        """
        return self._avg_prices[rarity]

    def _calc_avg_market_price(self, rarity):
        """
                Calculate the average market price of a certain card rarity

                :param rarity: String with a rarity that matches the Card objects
                :return: Double with the average market price
                """
        # Retrieve all cards of given rarity
        card_list = self.all_cards_of_rarity(rarity)
        total = 0

        # Calculate average market price
        for card in card_list:
            try:
                product_id = card["productId"]
                price_data = next((card for card in self._card_prices if card["productId"] == product_id), None)
                # market_price is stored as a string with a $ in front
                total += float(price_data['marketPrice'])
            except (ValueError, TypeError):
                logging.warning("Non-numeric price value encountered: {}".format(price_data['marketPrice']))
        return round(total / len(card_list), 2)

    def all_cards_of_rarity(self, rarity):
        """
        Gets all cards of a certain rarity for the set

        :param rarity: String with a rarity that matches the Card objects
        :return: List of all cards of the given rarity
        """
        return [card for card in self._card_list if card["extendedData"][1]["value"] == rarity]

    @property
    def rarities(self):
        return self._rarities
