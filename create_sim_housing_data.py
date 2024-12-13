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
NUM_HOUSES_FROM_1000000_TO_1499999 = [(1000000, 1499999), 2782676]
NUM_HOUSES_FROM_1500000_TO_1749999 = [(1500000, 1749999), 500000]
NUM_HOUSES_OVER_1749999 = [(1750000, 2999999), 390000]
NUM_HOUSES_OVER_2999999 = [(3000000, 9999999), 100000]
NUM_HOUSES_OVER_9999999 = [(10000000, 49999999), 9500]
NUM_HOUSES_OVER_49999999 = [(50000000, MOST_EXPENSIVE_HOUSE_PRICE), 500]

## Generate house prices efficiently with NumPy

class HousePriceDataGenerator:
    def __init__(self, house_prices: list=[]):
        # Ensure the input house_prices is a list of integers
        if not isinstance(house_prices, list):
            raise TypeError("house_prices must be a list")
        if not all(isinstance(price, int) for price in house_prices):
            raise TypeError("All elements in house_prices must be integers")
        house_prices.sort()
        # initialize constants
        self.house_ranges_totals = [NUM_HOUSES_UNDER_50000,
                      NUM_HOUSES_FROM_50000_TO_99999,
                      NUM_HOUSES_FROM_100000_TO_299999,
                      NUM_HOUSES_FROM_300000_TO_499999,
                      NUM_HOUSES_FROM_500000_TO_749999,
                      NUM_HOUSES_FROM_750000_TO_999999,
                      NUM_HOUSES_FROM_1000000_TO_1499999,
                      NUM_HOUSES_FROM_1500000_TO_1749999,
                      NUM_HOUSES_OVER_1749999,
                      NUM_HOUSES_OVER_2999999,
                      NUM_HOUSES_OVER_9999999,
                      NUM_HOUSES_OVER_49999999]
        
        # Initialize empty array
        self._house_prices = np.array(house_prices)
    
    @property
    def house_prices(self):
        if self._house_prices.size == 0:
            for price_range, num_houses in self.house_ranges_totals:
                # Generate random house prices within the range
                rand_house_prices = np.random.randint(
                    price_range[0], price_range[1] + 1, size=num_houses, dtype=np.int32
                )
                log_rand_house_prices = np.log(rand_house_prices)
                corr_rand_house_prices = log_rand_house_prices * ((15127188.177767897461941497007833 - 2019.4905985417228095571241466346)/51523067)
                corr_rand_house_prices.sort()
                self._house_prices = np.concatenate((self._house_prices, corr_rand_house_prices), axis=None)
        print(self._house_prices.size)
        return self._house_prices.tolist()

    @house_prices.setter
    def house_prices(self, val):
        if not isinstance(val, list):
            raise TypeError("house_prices must be a list")
        if not all(isinstance(price, int) for price in val):
            raise TypeError("All elements in house_prices must be integers")
        val.sort()
        self._house_prices = val


# 2019.4905985417228095571241466346
# 15,127,188.177767897461941497007833

# 51523068

# (0, 2019.4905985417228095571241466346)
# (51523067, 15,127,188.177767897461941497007833)

# m = 15,127,188.177767897461941497007833 - 2019.4905985417228095571241466346 / 51523067 - 0