import pandas as pd
import matplotlib.pyplot as plt

# Weekly screen time:
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
screen_time_hours = [4, 5.5, 6, 4.5, 7, 8, 6.5]  # ✅ Variable is now clearly named

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    screen_time_hours,        # ✅ Use correct variable name
    labels=days,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True,
    explode=[0.02]*7
)

plt.title('Screen Time Distribution (Pie Chart)')
plt.tight_layout()
plt.show()
