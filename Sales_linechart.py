import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Loading the CSV file
data = pd.read_csv('sales.csv')

# Step 2: Plotting the data
plt.plot(data['Month'], data['Sales'], marker='o', linestyle='-', color='teal')

# Step 3: Customizing the chart
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales in USD')
plt.grid(True)

# Step 4: Showing the chart
plt.show()
