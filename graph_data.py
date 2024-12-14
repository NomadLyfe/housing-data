from create_sim_housing_data import HousePriceDataGenerator
import numpy as np
import matplotlib.pyplot as plt
from LinearRegression import LinearRegression

# Create an instance of HousePriceDataGenerator
house_market = HousePriceDataGenerator()
house_prices = house_market.house_prices # Y
houses_indices = np.arange(len(house_prices)) # X

# Plot the data using a scatter plot
plt.figure(figsize=(19, 9))
plt.scatter(range(len(house_prices)), house_prices, color='blue', s=0.5)  # s=1 makes the points small
# plt.xscale('log')
# plt.yscale('log')

# Create regression line
reg = LinearRegression(lr=0.01)
reg.fit(houses_indices.reshape(-1, 1), house_prices)
y_pred_line = reg.predict(houses_indices.reshape(-1, 1))

# Set labels and title
plt.title('Scatter Plot of Housing Prices')
plt.xlabel('House Index (from lowest to highest price)')
plt.ylabel('House Price (USD)')
plt.tight_layout()
plt.xlim(-10000, 52000000)
plt.ylim(-10000, 1500000)
# Show grid
plt.grid(True)
# Plot regression line
plt.plot(houses_indices, y_pred_line, color='black', linewidth=2, label='Prediction')
# Show plot
plt.show()
