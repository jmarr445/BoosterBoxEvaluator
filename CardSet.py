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
        self._total_cards = len(card_list)
        self._card_prices = card_prices["results"]
        self._rarities = []
        # Create separate rarities for VMax and Full Art Ultra Rares
        # Make a list of all rarities in the set
        for count, card in enumerate(card_list):
            card_name = card["name"].lower()
            curr_rarity = card["extendedData"][1]["value"]
            if curr_rarity.lower() == "ultra rare":
                if "vmax" in card_name:
                    self._card_list[count]["extendedData"][1]["value"] = "Ultra Rare (VMax)"
                elif "full art" in card_name:
                    self._card_list[count]["extendedData"][1]["value"] = "Ultra Rare (Full Art)"
            curr_rarity = card["extendedData"][1]["value"]
            if curr_rarity not in self._rarities:
                self._rarities.append(curr_rarity)
        # Calculate ratios of each rarity
        self._calc_rarity_ratios()
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
                logging.warning("Non-numeric price value encountered")
        return round(total / len(card_list), 2)

    def _calc_rarity_ratios(self):
        """Determine the number of cards for each rarity type + ratios"""
        self._num_cards_rarity = {}
        self._card_ratios = {}
        for card in self._card_list:
            curr_rarity = card["extendedData"][1]["value"]
            if curr_rarity not in self._num_cards_rarity.keys():
                self._num_cards_rarity[curr_rarity] = 1
            else:
                self._num_cards_rarity[curr_rarity] += 1
        for rarity in self._num_cards_rarity:
            self._card_ratios[rarity] = round(100 * self._num_cards_rarity[rarity] / self.total_cards, 1)

    def all_cards_of_rarity(self, rarity):
        """
        Gets all cards of a certain rarity for the set

        :param rarity: String with a rarity that matches the Card objects
        :return: List of all cards of the given rarity
        """
        return [card for card in self._card_list if card["extendedData"][1]["value"] == rarity]

    @property
    def card_ratios(self):
        return self._card_ratios

    @property
    def num_cards_rarity(self):
        return self._num_cards_rarity

    @property
    def rarities(self):
        return self._rarities

    @property
    def total_cards(self):
        return self._total_cards
