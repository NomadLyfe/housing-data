import numpy as np

# data from 2023 cencus
# https://data.census.gov/table?t=Housing%20Value%20and%20Purchase%20Price&g=010XX00US&y=2023
CHEAPEST_HOUSE_PRICE = 20000
MOST_EXPENSIVE_HOUSE_PRICE = 295000000
NUM_HOUSES_UNDER_50000 = [(CHEAPEST_HOUSE_PRICE, 49999),1355175]
NUM_HOUSES_FROM_50000_TO_99999 = [(50000, 99999), 1917055]
NUM_HOUSES_FROM_100000_TO_299999 = [(100000, 299999), 16150351]
NUM_HOUSES_FROM_300000_TO_499999 = [(300000, 499999), 15444179]
NUM_HOUSES_FROM_500000_TO_749999 = [(500000, 749999), 8913516]
NUM_HOUSES_FROM_750000_TO_999999 = [(750000, 999999), 3960116]
NUM_HOUSES_OVER_999999 = [(1000000, MOST_EXPENSIVE_HOUSE_PRICE), 3882676]

## Generate house prices efficiently with NumPy

class HousePriceDataGenerator:
    def __init__(self, house_prices: list=[]):
        # Ensure the input house_prices is a list of integers
        if not isinstance(house_prices, list):
            raise TypeError("house_prices must be a list")
        if not all(isinstance(price, int) for price in house_prices):
            raise TypeError("All elements in house_prices must be integers")
        
        # initialize constants
        self.house_ranges_totals = [NUM_HOUSES_UNDER_50000,
                      NUM_HOUSES_FROM_50000_TO_99999,
                      NUM_HOUSES_FROM_100000_TO_299999,
                      NUM_HOUSES_FROM_300000_TO_499999,
                      NUM_HOUSES_FROM_500000_TO_749999,
                      NUM_HOUSES_FROM_750000_TO_999999,
                      NUM_HOUSES_OVER_999999]
        
        # Initialize empty array
        self._house_prices = house_prices
    
    @property
    def house_prices(self):
        if not self._house_prices:
            for price_range, num_houses in self.house_ranges_totals:
                # Generate random house prices within the range
                rand_house_prices = np.random.randint(
                    price_range[0], price_range[1] + 1, size=num_houses, dtype=np.int32
                )
                self._house_prices.extend(rand_house_prices)
        return self._house_prices

    @house_prices.setter
    def house_prices(self, val):
        if not isinstance(val, list):
            raise TypeError("house_prices must be a list")
        if not all(isinstance(price, int) for price in val):
            raise TypeError("All elements in house_prices must be integers")
        self._house_prices = val
