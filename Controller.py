from ApplicationManager import ApplicationManager
from View import MainView
from WebScraper import WebScraper


class Controller:
    """Controller for the application"""

    def __init__(self, root):
        """Initialize the controller"""
        self.webscraper = WebScraper.get_instance()
        self.view = MainView(self, root)
        self.model = ApplicationManager()

    def calculate_price(self):
        """
        Calculate the expected value of the booster box based on what is entered in the view entry widgets
        """
        self.view.box_prc_msg = str(self.model.calc_ev(self.view.rarity_amts))

    def get_set_list_names(self):
        """
        Retrieves all set list names

        :return: A list of all set list names
        """
        return self.webscraper.get_set_list_names()

    def update_current_set(self, event):
        """Updates the curr set information when a new list item is selected"""
        self.model.update_current_set(event)
        self.view.curr_set_msg = self.model.curr_set_message
        self.view.clear_set_info()
        self.view.update_set_info(self.model.rarities, self.model.avg_price_msg)
