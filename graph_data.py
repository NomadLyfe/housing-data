from create_sim_housing_data import HousePriceDataGenerator
import matplotlib.pyplot as plt

# Create an instance of HousePriceDataGenerator
house_market = HousePriceDataGenerator()  # This will generate house prices automatically

# Get the generated house prices
house_prices = house_market.house_prices
# house_prices = [1, 4, 8, 10, 11, 12, 12, 12, 12, 13, 14, 18, 23, 30]

# Plot the data using a scatter plot
plt.figure(figsize=(19, 9))
plt.scatter(range(len(house_prices)), house_prices, color='blue', s=1)  # s=1 makes the points small
# plt.xscale('log')
# plt.yscale('log')

# Set labels and title
plt.title('Scatter Plot of Housing Prices')
plt.xlabel('House Index (from lowest to highest price)')
plt.ylabel('House Price (USD)')
plt.tight_layout()
# Show grid and plot
plt.grid(True)
plt.show()
