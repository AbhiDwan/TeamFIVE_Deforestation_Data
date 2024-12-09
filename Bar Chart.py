import numpy as np
import matplotlib.pyplot as plt

# Data: Deforestation over a decade in 6 countries in hectares.
countries = np.array(["USA", "Canada", "India", "Argentina", "Mexico", "China"])
Hectares = np.array([1200000, 3000000, 5000000, 2900000, 3200000, 3500000])

# Create indices for the x-axis
indices = np.arange(len(countries))

# Bar width
bar_width = 0.4

# Create the bar graph
plt.figure(figsize=(12, 6))
plt.bar(indices - bar_width / 2, Hectares, bar_width, label='Area lost due to Deforestation (Hectares)', color='blue')

# Add labels, title, and legend
plt.xticks(indices, countries)
plt.xlabel("Countries", fontsize=12)
plt.ylabel("Area(million hectares)", fontsize=12)
plt.title("Area lost due to Deforestation", fontsize=16)
plt.legend()

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()