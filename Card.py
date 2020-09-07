class Card:
    """
    This class models a card from tcgplayer
    """

    def __init__(self, product, rarity, number, market_price):
        """
        Initialize a new card with the provided properties

        :param product: Card name
        :param rarity: Rarity
        :param number: Number in the set. Expected format is number/total_number
        :param market_price: Current market price
        """

        self._product = product
        self._rarity = rarity
        self._number = number
        self._market_price = market_price

    @property
    def product(self):
        return self._product

    @property
    def rarity(self):
        return self._rarity

    @property
    def number(self):
        return self._number

    @property
    def market_price(self):
        return self._market_price
