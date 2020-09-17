import requests


class APICaller:
    """This class lets you make API calls to TCGPlayer"""

    def __init__(self):
        """Initialize APICaller"""
        # Base URL for API calls
        self._base_URL = "https://api.tcgplayer.com/"

        # Define standard headers for calls
        self._headers = {"User-Agent": "Booster Box Evaluator"}

        data = "grant_type=client_credentials&client_id=183c425d-7217-4859-b9b5-f0e90c664e47&client_secret=7fa90350" \
               "-5721-40c3-ae35-36b834ac9e72 "
        response = requests.post("https://api.tcgplayer.com/token", data=data)
        self._bearer_token = response.json()['access_token']

    def get_all_sets(self):
        """Returns a list with all Pokemon set names"""
        url = self._base_URL + "catalog/categories/3/groups"

        response = requests.request("GET", url, headers=self._headers)
        print(response.text)


caller = APICaller()
caller.get_all_sets()
