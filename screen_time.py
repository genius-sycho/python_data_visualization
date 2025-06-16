import pandas as pd
import matplotlib.pyplot as plt

# Weekly screen time:
data = {
    "Day" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Screen Time (hours)" : [4, 5.5, 6, 4.5, 7, 8, 6.5,]
    }
# Creating DataFrame
df = pd.DataFrame(data)
# printing table
print(df)
#plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Day"], df["Screen Time (hours)"], color="lightgreen")
plt.title("Weekly Screen Time")
plt.xlabel("Day of the week")
plt.ylabel("Hours")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()