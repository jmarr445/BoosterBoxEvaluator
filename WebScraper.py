import requests
from bs4 import BeautifulSoup

from Card import Card


class WebScraper:
    """
    This class provides methods to retrieve pricing information and parse it for relevant data
    """

    def __init__(self):
        """ Initialize an instance """

        # Base URL
        self._URL = "https://shop.tcgplayer.com/price-guide/pokemon/"

        # Info
        self._set_info = {}

        # Retrieve contents of the Set drop down menu
        page = requests.get(self._URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        price_guide_drop_down = soup.find('select', attrs={"class": "priceGuideDropDown", "id": "set"}) \
            .find_all('option')

        # Put the text and value attributes for each set into lists
        self._set_list = []
        self._set_list_names = []
        for card_set in price_guide_drop_down:
            self._set_list.append(card_set['value'])
            self._set_list_names.append(card_set.text.strip())

    def get_set_list_names(self):
        """ Returns the list of set list names """
        return self._set_list_names

    def update_page(self, ind):
        """
        Update _set_info based on the currently selected set

        :param ind: The index of the selected set in the list box
        """
        page = requests.get(self._URL + self._set_list[ind])
        soup = BeautifulSoup(page.content, 'html.parser')
        self._set_info["card_list"] = self._get_cards(soup)

    def _get_cards(self, soup):
        """
        Parses the webpage and retrieves all card data

        :param soup: Beautiful Soup 4 webpage
        :return: List of cards
        """
        card_list = []
        card_tags = soup.find("table", class_="priceGuideTable tablesorter").find("tbody") \
            .find_all("tr")
        # Initialize a card object for each card on the page
        for card in card_tags:
            card_list.append(
                Card(card.find("td", class_="product").text.strip(),
                     card.find("td", class_="rarity").text.strip(),
                     card.find("td", class_="number").text.strip(),
                     card.find("td", class_="marketPrice").text.strip())
            )
        return card_list

    @property
    def set_info(self):
        return self._set_info
