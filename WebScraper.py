import requests
from bs4 import BeautifulSoup


class WebScraper:
    """
    This class provides methods to retrieve pricing information and parse it for relevant data
    """

    def __init__(self):
        """ Initialize an instance """

        # Base URL
        self._URL = "https://shop.tcgplayer.com/price-guide/pokemon/"

        # Retrieve contents of the Set drop down menu
        _page = requests.get(self._URL)
        _soup = BeautifulSoup(_page.content, 'html.parser')
        _price_guide_drop_down = _soup.find('select', attrs={"class": "priceGuideDropDown", "id": "set"}) \
            .find_all('option')

        # Put the text and value attributes for each set into lists
        self._set_list = []
        self._set_list_names = []
        for card_set in _price_guide_drop_down:
            self._set_list.append(card_set['value'])
            self._set_list_names.append(card_set.text.strip())

    def get_set_list_names(self):
        """
        Returns the list of set list names

        :return: Current set list names
        """
        return self._set_list_names


web_scraper = WebScraper()
