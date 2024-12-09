import numpy as np
import matplotlib.pyplot as plt

# Data: Country wise Deforestation (years)
countries = np.array(["USA", "Canada", "India", "Argentina", "Mexico", "China"])
Hectares = np.array([1200000, 3000000, 5000000, 2900000, 3200000, 3500000])

# Create a pie chart for Healthcare Spending
plt.figure(figsize=(8, 8))

# Subplot for Healthcare Spending
plt.pie(Hectares, labels=countries, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors)
plt.title("Country wise Deforestation")


# Adjust layout and display
plt.show()