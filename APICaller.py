import requests


class APICaller:
    """This class lets you make API calls to TCGPlayer"""

    def __init__(self):
        """Initialize APICaller"""
        # Base URL for API calls
        self._base_URL = "https://api.tcgplayer.com/"

        data = "grant_type=client_credentials&client_id=183c425d-7217-4859-b9b5-f0e90c664e47&client_secret=7fa90350" \
               "-5721-40c3-ae35-36b834ac9e72 "
        response = requests.post("https://api.tcgplayer.com/token", data=data)
        self._bearer_token = response.json()['access_token']

        # Define standard headers for calls
        self._headers = {
            "User-Agent": "Booster Box Evaluator",
            "Authorization": "bearer "+self._bearer_token
        }

    def get_all_sets(self):
        """Returns a list with all Pokemon set names"""
        url = self._base_URL + "catalog/categories/3/groups"

        querystring = {"limit": "1000"}

        response = requests.request("GET", url, headers=self._headers, params=querystring)
        return response.json()

    def get_card_prices(self, group_id):
        """
        Retrieve all price information for cards in a given set.

        :param group_id: The groupId of the set
        :return: List with price information
        """
        url = self._base_URL + "pricing/group/" + str(group_id)

        return requests.request("GET", url, headers=self._headers).json()

    def get_cards_for_set(self, group_id):
        """
        Returns a dict with all of the card prices for a given groupID.

        :param group_id: groupID of the desired set.
        :return: All card prices
        """
        url = self._base_URL + "catalog/products"

        query_string = {"groupId": group_id, "getExtendedFields": "true", "productTypes": "cards", "limit": "100"}

        return self._retrieve_all_results(url, query_string)

    def _retrieve_all_results(self, url, query_string):
        """
        Retrieve all results for a given API call. TCGPlayer has a 100 response limit per call, so this retrieves
        all results beyond just the first 100

        :param url: String with the endpoint to hit
        :param query_string: Dictionary with the query params
        :return: The results section of the response body
        """
        # Request first batch of cards
        response = requests.request("GET", url, headers=self._headers, params=query_string).json()
        val = response
        total_items = response["totalItems"] - 100
        query_string["offset"] = "100"

        # Repeat the call while changing the offset until all items have been retrieved
        while total_items >= 0:
            response = requests.request("GET", url, headers=self._headers, params=query_string).json()
            val["results"] += response["results"]
            total_items -= 100
            query_string["offset"] = str(int(query_string["offset"]) + 100)

        return val["results"]
