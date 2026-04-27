class NumberProcessor:
    """Handles the core logic for identifying number parity"""

    def separate_evens(self, integer_list):
        """Filters a list to return only even integers."""
        return [number for number in integer_list if number % 2 == 0]

    def separate_odds(self, integer_list):
        """Filters a list to return only odd integers."""
        return [number for number in integer_list if number % 2 != 0]
